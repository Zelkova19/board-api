from typing import Annotated
from fastapi import Depends


def get_task_repository():
    return TaskRepository()


class TaskRepository:
    def get_by_id(self, project_id: int):
        return project_id


TaskRepositoryDeps = Annotated[TaskRepository, Depends(get_task_repository)]
