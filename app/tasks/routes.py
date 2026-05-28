import logging

from fastapi import APIRouter, Depends, HTTPException


from .service import TaskServiceDeps

from .schema import TaskGetResponse, TaskPath


router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)


@router.get(
    "/{task_id}",
    description="""Получает задачу по ID, иначе возвращает None""",
    response_model=TaskGetResponse,
)
def get_task(service: TaskServiceDeps, path: TaskPath = Depends()):
    res = service.get(path.task_id)
    if not res:
        raise HTTPException(404, "Не найдено")
    logger.info("ID: %s", res, extra={"user_id": 1})
    return TaskGetResponse(id=res)
