from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app import schemas, queries

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=list[schemas.users.User])
def get_users():
    users: list[schemas.users.User] = queries.users.get_all_users()
    return users


@router.post('/')
def post_user(user: schemas.users.User):
    user_exists: schemas.users.User | None = queries.users.get_user_using_email(user.email)
    if user_exists:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User with this email already exists!')
    else:
        queries.users.insert_user(user)
        return JSONResponse({'result': True}, status_code=status.HTTP_201_CREATED)
