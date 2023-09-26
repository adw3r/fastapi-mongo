import bson
import pymongo
from pymongo.results import UpdateResult, DeleteResult

from app import database, schemas


def get_all_users() -> list[schemas.users.User] | list[None]:
    users: pymongo.cursor.Cursor = database.CLIENT_LOCAL_USERS.find()
    users: list[schemas.users.User] = [schemas.users.User(**user) for user in users]
    return users


def get_user_using_email(email: str) -> schemas.users.User | None:
    find_result = database.CLIENT_LOCAL_USERS.find_one({'email': email})
    if not find_result:
        return None
    user = schemas.users.User(**find_result)
    return user


def get_user_using_id(user_id: str) -> schemas.users.User | None:
    find_result = database.CLIENT_LOCAL_USERS.find_one({'_id': bson.ObjectId(user_id)})
    if not find_result:
        return None
    user = schemas.users.User(**find_result)
    return user


def insert_user(user: schemas.users.PostUser):
    database.CLIENT_LOCAL_USERS.insert_one(user.model_dump())


def update_user(user_id: str, user: schemas.users.PatchUser) -> UpdateResult:
    result = database.CLIENT_LOCAL_USERS.update(
        {'_id': bson.ObjectId(user_id)}, {'$set': user.model_dump()}
    )
    return result


def delete_user(user_id: str) -> DeleteResult:
    result = database.CLIENT_LOCAL_USERS.delete_one({'_id': bson.ObjectId(user_id)})
    return result


def find_and_update_user(user_id: str, user: schemas.users.PatchUser):
    ...


def find_and_delete_user(user_id: str, user: schemas.users.PatchUser):
    ...
