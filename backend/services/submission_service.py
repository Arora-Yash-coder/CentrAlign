from config.db_config import get_db
from bson import ObjectId
from datetime import datetime


def save_submission(form_id: str, responses: dict):
    """
    Stores a single form submission.
    responses may include image URLs already uploaded to Cloudinary.
    """
    db = get_db()

    doc = {
        "form_id": str(form_id),
        "responses": responses,
        "submitted_at": datetime.utcnow()
    }

    result = db.submissions.insert_one(doc)
    return str(result.inserted_id)


def get_submissions_for_form(form_id: str, user_id: str):
    """
    Prevent unauthorized access.
    """
    db = get_db()

    # Check form ownership
    form = db.forms.find_one({"_id": ObjectId(form_id)})
    if not form or str(form["user_id"]) != str(user_id):
        return []

    cursor = db.submissions.find({"form_id": str(form_id)})

    return [
        {
            "id": str(s["_id"]),
            "responses": s.get("responses"),
            "submitted_at": s.get("submitted_at")
        }
        for s in cursor
    ]


def get_all_user_submissions(user_id: str):
    """
    Dashboard-friendly structure:
    {
       form_id: [...submissions]
    }
    """
    db = get_db()

    forms = list(db.forms.find({"user_id": user_id}, {"_id": 1}))
    form_ids = {str(f["_id"]) for f in forms}

    cursor = db.submissions.find({"form_id": {"$in": list(form_ids)}})

    grouped = {fid: [] for fid in form_ids}

    for doc in cursor:
        fid = doc["form_id"]
        grouped[fid].append({
            "id": str(doc["_id"]),
            "responses": doc.get("responses"),
            "submitted_at": doc.get("submitted_at")
        })

    return grouped
