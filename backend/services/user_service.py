from config.db_config import get_db
from utils.hashing import hash_password, verify_password
from utils.jwt_handler import create_access_token
from models.user import UserCreate
from bson import ObjectId
from datetime import datetime


def create_user(payload: UserCreate):
    db = get_db()

    # check if user exists
    existing = db.users.find_one({"email": payload.email})
    if existing:
        return None

    doc = {
        "email": payload.email,
        "password_hash": hash_password(payload.password),
        "created_at": datetime.utcnow()
    }

    res = db.users.insert_one(doc)
    return str(res.inserted_id)


def authenticate_user(email: str, password: str):
    db = get_db()

    user = db.users.find_one({"email": email})
    if not user:
        return None

    if not verify_password(password, user["password_hash"]):
        return None

    return user


def generate_jwt_token(user_id: str):
    token = create_access_token({"user_id": str(user_id)})
    return token
