
from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="GenAI Chat API",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")


@app.get("/")
def home():
    return {"message": "GenAI Chat API is running"}