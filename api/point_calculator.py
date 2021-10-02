from fastapi import APIRouter
from db import db
router = APIRouter()


@router.get("/hello/world")
def hello_world():
    print(db)
    return "Hi"