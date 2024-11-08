from fastapi import FastAPI, Request
from chatbot_routes import router
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)

# Run the app using the following command:
# python app/main.py