from pydantic import BaseModel


class MemoryRequest(BaseModel):
    prompt: str
