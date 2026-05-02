from enum import StrEnum
from fastapi import HTTPException, APIRouter, Request


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизован")


router = APIRouter(prefix="/posts")


class SortOrder(StrEnum):
    asc = "asc"
    desc = "desc"


@router.get("/{post_id}")
def get_post(post_id: int):
    return {"id": post_id}


@router.put("/{post_id}")
def put_post(post_id: int):
    return {f"update post {post_id}": "success"}


@router.delete("/{post_id}")
def delete_post(post_id: int):
    return {f"delete post {post_id}": "success"}


@router.post("/")
async def creat_post(
    request: Request,
):
    data = await request.json()
    return data
