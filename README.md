# FastAPI Chatbot Project

This is a chatbot application built using the FastAPI web framework. It uses Google Gemini’s Multi-Modal feature, so you can upload files like PDFs, Python code, TXT, HTML, CSS, images (PNG, WEBP, JPEG), or Markdown. Then, you can ask questions about the content.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Poetry (for dependency management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aasherkamal216/FastAPI-Chatbot-Project.git
   ```
2. Navigate to the project directory:

   ```bash
    cd chatbot-project
   ```
3. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```
4. Create a `.env` file and add your Google API key like this:

   ```bash
   GOOGLE_API_KEY="YOUR_API_KEY"
   ```

5. Start the FastAPI server:

   ```bash
   poetry run uvicorn app.main:app --reload
   ```
6. Open a web browser and navigate to http://localhost:8000 to access the chatbot interface.

### Usage
* Type a message in the chat window and press Enter to send it to the chatbot.
* Upload a file to the chatbot by clicking the "Choose File" button in the sidebar.
* The file will be uploaded to the server and sent to the LLM.
* You can ask questions about the uploaded file or any other topic.
* To reset the chat, click the "Reset Conversation" button in the sidebar.