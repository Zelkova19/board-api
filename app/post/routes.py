from enum import StrEnum
from fastapi import HTTPException, APIRouter, Request, Query


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


@router.get("/")
def get_posts(
    limit: int = 10,
    offset: int = Query(0, ge=0),
    tags: list[str] = Query([]),
    order: SortOrder = SortOrder.asc,
):
    return {"limit": limit, "offset": offset, "tags": tags, "order": order}


@router.post("/")
async def creat_post(
    request: Request,
):
    data = await request.json()
    return data
