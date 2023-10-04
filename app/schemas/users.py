from typing import Any
from typing import Annotated, Union

from bson import ObjectId
from pydantic import BaseModel
from pydantic import EmailStr, Field, PlainSerializer, AfterValidator, WithJsonSchema


def validate_object_id(v: Any) -> ObjectId:
    if isinstance(v, ObjectId):
        return v
    if ObjectId.is_valid(v):
        return ObjectId(v)
    raise ValueError("Invalid ObjectId")


PyObjectId = Annotated[
    Union[str, ObjectId],
    AfterValidator(validate_object_id),
    PlainSerializer(lambda x: str(x), return_type=str),
    WithJsonSchema({"type": "string"}, mode="serialization"),
]


class User(BaseModel):
    id: PyObjectId = Field(alias="_id", serialization_alias='id')
    name: str = Field(...)
    email: EmailStr = Field(...)
    phone: str = Field(...)

    class Config:
        arbitrary_types_allowed = True


class PostUser(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    phone: str = Field(...)
    password: str = Field(...)


class PutUser(PostUser):
    ...


class PatchUser(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None
