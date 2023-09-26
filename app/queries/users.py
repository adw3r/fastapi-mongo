import pymongo

from app import database, schemas


def get_all_users() -> list[schemas.users.User]:
    users: pymongo.cursor.Cursor = database.CLIENT_LOCAL_USERS.find()
    users: list[schemas.users.User] = [schemas.users.User(**user) for user in users]
    return users


def get_user_using_email(email: str) -> schemas.users.User | None:
    find_result = database.CLIENT_LOCAL_USERS.find_one({'email': email})
    if not find_result:
        return None
    user = schemas.users.User(**find_result)
    return user


def insert_user(user: schemas.users.User):
    database.CLIENT_LOCAL_USERS.insert_one(user.model_dump())