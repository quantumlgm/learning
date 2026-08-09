from typing import Dict
from schemas import UserInDB


db_users: Dict[str, UserInDB] = {}


def get_user_by_email(email: str) -> UserInDB | None:
    return db_users.get(email)