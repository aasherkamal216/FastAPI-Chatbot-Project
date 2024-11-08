from fastapi import APIRouter, UploadFile, File, Body, HTTPException, status
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os, dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
dotenv.load_dotenv()

# Initialize the API router
router = APIRouter(
    prefix="/chatbot",

)

# Configure the API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# Set up the model
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="You are a helpful assistant for question answering tasks.",
    generation_config={"temperature": 0.5},
)

# Initialize the chat history and gemini messages
gemini_messages = []
chat_history = []

# router to upload a file
@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file to the chatbot to be used in the conversation.
    Currently supports PDF, Python, Plain Text, HTML, CSS, and Markdown.
    """
    valid_formats = [
        "application/pdf",
        "text/x-python",
        "text/plain",
        "text/html",
        "text/css",
        "text/md",
        "image/webp",
        "image/png",
        "image/jpeg"
    ]
    if file.content_type in valid_formats:
  
        uploaded_file = genai.upload_file(path=file.file, mime_type=file.content_type)
        logger.info("File: %s uploaded successfully", file.filename)
        
        message = {
            "role": "user",
            "parts": [uploaded_file],
        }
        gemini_messages.append(message)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "File uploaded successfully"},
        )

    else:
        return HTTPException(
            status_code=400,
            detail="Invalid file format. Only PDF, Python, Plain Text, HTML, CSS, and Markdown are supported.",
        )

# chat with the model
@router.post("/chat")
async def chat(question: str = Body(embed=True)):
    # Add the question to the chat history and gemini messages
    gemini_messages.append(
        {
            "role": "user",
            "parts": [question]
        }
        )
    chat_history.append({"role": "user", "content": question})

    # Generate the response
    response = await model.generate_content_async(gemini_messages)
    gemini_messages.append(
        {
            "role": "model",
            "parts": [response.text]
        })
    chat_history.append({"role": "assistant", "content": response.text})
        
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"response": response.text},
    )

# get the chat history
@router.get("/chat-history")
async def conversation():
    return {"chat_history": chat_history}

# reset the conversation
@router.delete("/reset")
async def reset():
    global chat_history
    global gemini_messages
    chat_history = []
    gemini_messages = []

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Chat history reset successfully"},
    )
