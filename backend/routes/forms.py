from fastapi import APIRouter, HTTPException, Depends
from models.form import FormCreate
from services.form_service import (
    generate_form_schema,
    save_form,
    get_user_forms,
    get_form_by_id
)
from utils.jwt_handler import get_current_user_id

router = APIRouter()

@router.post("/generate")
def generate_form(payload: FormCreate, user_id: str = Depends(get_current_user_id)):
    schema = generate_form_schema(payload.prompt, user_id)
    form_id = save_form(schema, user_id)
    return {"status": "success", "form_id": form_id, "schema": schema}

@router.get("/")
def list_forms(user_id: str = Depends(get_current_user_id)):
    forms = get_user_forms(user_id)
    return {"forms": forms}

@router.get("/{form_id}")
def get_form(form_id: str):
    form = get_form_by_id(form_id)
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    return {"form": form}
