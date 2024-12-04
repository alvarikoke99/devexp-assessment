from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class To(BaseModel):
    name: str
    phone: str
    id: str

class Message(BaseModel):
    from_: str = Field(..., alias="from")
    content: str
    id: str
    status: str
    created_at: datetime = Field(..., alias="createdAt")
    delivered_at: Optional[datetime] = Field(None, alias="deliveredAt")
    to: To

class MessagesResponse(BaseModel):
    messages: List[Message]
    page: int
    quantity_per_page: int = Field(..., alias="quantityPerPage")

class CreateMessageRequest(BaseModel):
    from_: str = Field(..., alias="from")
    to: str 
    content: str

class CreateContactRequest(BaseModel):
    name: str
    phone: str

class UpdateContactRequest(BaseModel):
    name: str
    phone: str

class Contact(BaseModel):
    id: str
    name: str
    phone: str

class ContactsResponse(BaseModel):
    contacts: List[Contact]
    page: int
    quantity_per_page: int = Field(..., alias="quantityPerPage")

class WebhookDeliveryStatus(BaseModel):
    message_id: str = Field(..., alias="messageId")
    status: str
    delivered_at: Optional[datetime] = Field(None, alias="deliveredAt")

class Webhook(BaseModel):
    event: str
    data: WebhookDeliveryStatus