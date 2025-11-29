from pydantic import BaseModel


class FormCreate(BaseModel):
    prompt: str
