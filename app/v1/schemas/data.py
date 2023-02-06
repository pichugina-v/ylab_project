from pydantic import BaseModel

class DataTestDetail(BaseModel):
    message: str

class TaskDetail(BaseModel):
    status: str
    task_id: str
