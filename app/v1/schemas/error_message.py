from pydantic import BaseModel


class Message404(BaseModel):
    detail: str


class MessageDeleted(BaseModel):
    status: str
    message: str
