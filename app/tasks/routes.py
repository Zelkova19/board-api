from fastapi import APIRouter, Depends

from .service import TaskServiceDeps

from .schema import TaskGetResponse, TaskPath

router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])


@router.get(
    "/{task_id}",
    description="""Получает задачу по ID, иначе возвращает None""",
    response_model=TaskGetResponse,
)
def get_task(service: TaskServiceDeps, path: TaskPath = Depends()):
    res = service.get(path.task_id)
    return TaskGetResponse(id=res)
