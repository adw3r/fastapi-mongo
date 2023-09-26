from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app import schemas, queries

router = APIRouter(prefix='/users', tags=['Users'])


# получение всех юзеров
@router.get('/')
def get_users():
    users: list[schemas.users.User] | list = queries.users.get_all_users()
    return users


# получение юзера по почте
@router.get('/{email}', response_model=schemas.users.User)
def get_user_using_email(email):
    user_exists: schemas.users.User | None = queries.users.get_user_using_email(email)
    if user_exists:
        return user_exists
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not exists!')


# вставка юзера
@router.post('/')
def post_user(user: schemas.users.PostUser):
    user_exists: schemas.users.User | None = queries.users.get_user_using_email(user.email)
    if user_exists:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User with this email already exists!')
    else:
        queries.users.insert_user(user)
        return JSONResponse({'result': True}, status_code=status.HTTP_201_CREATED)


# частичная замена данных юзера
@router.patch('/{user_id}')
def patch_user(user_id: str, user: schemas.users.PatchUser):
    user_exists: schemas.users.User | None = queries.users.get_user_using_id(user_id)
    if not user_exists:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not exists!')
    else:
        updated_user: schemas.users.User = queries.users.update_user(user)
        return updated_user


# удаление юзера
@router.delete('/{user_id}')
def delete_user():
    ...
