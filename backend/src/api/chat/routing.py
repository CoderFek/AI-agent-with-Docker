from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from api.db import get_session
from api.ai.services import generate_email_message
from api.ai.schemas import EmailMessageSchema
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem

router = APIRouter()

# /api/chats/
@router.get('/')
def chat_health():
    return {"status": "ok"}

# /api/chats/recent/
# curl http://localhost:8080/api/chats/recent/
@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results

# HTTP post -> payload = {'message': 'Hello, world!'}
# curl -X POST http://localhost:8080/api/chats/ -H "Content-Type: application/json" -d '{"message": "Hello, world!"}'

# curl -X POST http://localhost:8080/api/chats/ -H "Content-Type: application/json" -d '{"message": "Give me a summary of why it is good to go outside"}'

@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session),
    ):
    data = payload.model_dump() # pydantic dict
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    #session.refresh(obj) # ensures id/primary key is added to obj instance

    ai_response = generate_email_message(payload.message)
    return ai_response
