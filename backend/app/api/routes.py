
from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import gemini_service


router = APIRouter()

@router.get("/health")
def health():
    return {"status": "healthy"}

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = gemini_service.generate(request.message)

    return ChatResponse(response=answer)