from sqlmodel import SQLModel, Field

class ChatMessagePayload(BaseModel):
    # pydantic model
    message: str

class ChatMessage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str