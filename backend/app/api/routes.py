

from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import gemini_service

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "healthy"}

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    
    # print terminal me ayega
    print("[DEBUG] Request object:", request)
    print("[DEBUG] Request type:", type(request))
    print("[DEBUG] Request dictionary:", request.model_dump())
    print("[DEBUG] User message:", request.message)
    answer = gemini_service.generate(request.message)

    # this response variable comes from chat/ChatResponse
    return ChatResponse(response=answer)