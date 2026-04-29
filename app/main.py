from enum import StrEnum
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()


class UnauthHTTPException(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Не авторизован")


class SortOrder(StrEnum):
    asc = "asc"
    desc = "desc"


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return {"id": post_id}


@app.get("/posts")
def get_posts(
    limit: int = 10,
    offset: int = Query(0, ge=0),
    tags: list[str] = Query([]),
    order: SortOrder = SortOrder.asc,
):
    return {"limit": limit, "offset": offset, "tags": tags, "order": order}
