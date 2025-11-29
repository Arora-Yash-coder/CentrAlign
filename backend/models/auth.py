from pydantic import BaseModel


class TokenPayload(BaseModel):
    user_id: str


class TokenResponse(BaseModel):
    token: str
    user_id: str
