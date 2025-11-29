from fastapi import APIRouter, HTTPException, Depends
from services.submission_service import (
    save_submission,
    get_submissions_for_form,
    get_all_user_submissions
)
from utils.jwt_handler import get_current_user_id

router = APIRouter()

@router.post("/{form_id}")
def submit_form(form_id: str, payload: dict):
    """
    Public endpoint – does NOT require auth.
    Stores form responses including image URLs.
    """
    submission_id = save_submission(form_id, payload)
    return {"status": "success", "submission_id": submission_id}

@router.get("/form/{form_id}")
def list_submissions_for_form(form_id: str, user_id: str = Depends(get_current_user_id)):
    """
    Only the owner should see their form's submissions.
    """
    submissions = get_submissions_for_form(form_id, user_id)
    return {"submissions": submissions}

@router.get("/")
def all_submissions(user_id: str = Depends(get_current_user_id)):
    """
    Dashboard: grouped submissions for logged-in user.
    """
    data = get_all_user_submissions(user_id)
    return {"submissions": data}
