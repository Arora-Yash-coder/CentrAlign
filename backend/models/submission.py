from pydantic import BaseModel
from typing import Any, Dict


class SubmissionCreate(BaseModel):
    responses: Dict[str, Any]
