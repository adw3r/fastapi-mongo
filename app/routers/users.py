from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app import database, schemas

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('/', response_model=list[schemas.users.User])
def get_users():
    users = database.CLIENT_LOCAL_USERS.find()
    return [user for user in users]


@router.post('/')
def post_user(user: schemas.users.User):
    existing_user = database.CLIENT_LOCAL_USERS.find_one({'email': user.email})
    if existing_user:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User with this email already exists!')

    database.CLIENT_LOCAL_USERS.insert_one(user.model_dump())
    return JSONResponse({'result': True}, status_code=status.HTTP_201_CREATED)
