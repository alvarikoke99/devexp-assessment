from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class Contact(BaseModel):
    id: str
    name: str
    phone: str

class Message(BaseModel):
    from_: str = Field(..., alias="from")
    content: str
    id: str
    status: str
    created_at: datetime = Field(..., alias="createdAt")
    delivered_at: Optional[datetime] = Field(None, alias="deliveredAt")
    to: str

class MessagesResponse(BaseModel):
    messages: List[Message]
    page: int
    quantityPerPage: int

class ContactListResponse(BaseModel):
    contacts: list[Contact]
    pageNumber: int
    pageSize: int