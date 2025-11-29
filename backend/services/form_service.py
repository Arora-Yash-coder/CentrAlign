from config.db_config import get_db
from services.ai_service import generate_form_schema
from services.embedding_service import embed_form_summary
from bson import ObjectId
from datetime import datetime


def save_form(schema: dict, user_id: str):
    """
    Stores:
    - JSON schema
    - auto-generated summary
    - embedding for retrieval
    """
    db = get_db()

    summary = " ".join([f.get("label", "") for f in schema.get("fields", [])])
    embedding = embed_form_summary(schema)

    form_doc = {
        "user_id": user_id,
        "schema": schema,
        "summary": summary,
        "embedding": embedding,
        "created_at": datetime.utcnow()
    }

    result = db.forms.insert_one(form_doc)
    return str(result.inserted_id)


def generate_form_schema(prompt: str, user_id: str):
    """
    Delegates to AI generator service (memory-aware schema generation).
    """
    return generate_form_schema(prompt, user_id)


def get_user_forms(user_id: str):
    db = get_db()
    forms = db.forms.find(
        {"user_id": user_id},
        {"schema": 1, "summary": 1, "created_at": 1}
    )

    return [
        {
            "id": str(f["_id"]),
            "summary": f.get("summary"),
            "created_at": f.get("created_at")
        }
        for f in forms
    ]


def get_form_by_id(form_id: str):
    db = get_db()
    doc = db.forms.find_one({"_id": ObjectId(form_id)})

    if not doc:
        return None

    return {
        "id": str(doc["_id"]),
        "schema": doc.get("schema"),
        "summary": doc.get("summary"),
        "created_at": doc.get("created_at")
    }
