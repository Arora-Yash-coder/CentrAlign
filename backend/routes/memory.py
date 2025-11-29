from fastapi import APIRouter, Depends
from services.memory_service import retrieve_relevant_forms
from utils.jwt_handler import get_current_user_id

router = APIRouter()

@router.post("/retrieve")
def retrieve_memory(data: dict, user_id: str = Depends(get_current_user_id)):
    """
    Input:
    {
        "prompt": "I need an internship hiring form with resume upload"
    }
    """
    prompt = data.get("prompt")
    results = retrieve_relevant_forms(prompt, user_id)
    return {"relevant_context": results}
