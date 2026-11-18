from pydantic import BaseModel, Field

# Frontend se aane wala message validate karega.
class ChatRequest(BaseModel):
    message: str = Field(min_length=1)

# Backend se frontend ko bheje jane wale response ka structure define karega.
class ChatResponse(BaseModel):
    response: str

    