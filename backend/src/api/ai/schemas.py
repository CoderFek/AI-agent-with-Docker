import os

from pydantic import BaseModel, Field

class EmailMessageSchema(BaseModel):
    subject: str
    contexts: str
    invalid_request: bool | None = Field(default = False)