from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
