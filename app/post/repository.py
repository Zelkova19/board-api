from typing import Annotated
from fastapi import Depends


def get_post_repository():
    return PostRepository()


class PostRepository:
    def get_by_id(self, project_id: int):
        return project_id


PostRepositoryDeps = Annotated[PostRepository, Depends(get_post_repository)]
