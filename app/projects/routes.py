from http import HTTPStatus
from fastapi import APIRouter, Depends

from .service import ProjectServiceDeps
from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectDeleteResponse,
    ProjectGetResponse,
    ProjectPath,
    ProjectUpdateResponse,
    ProjectUpdateRequest,
)


router = APIRouter(prefix="/v1/projects", tags=["Projects"])


@router.get(
    "/{project_id}",
    response_model=ProjectGetResponse,
    summary="Получить проект",
    description="""
    Получаем проект по его ID
    """,
)
def get_project(
    service: ProjectServiceDeps,
    path: ProjectPath = Depends(),
):
    res = service.get_project(path.project_id)
    return ProjectGetResponse(id=res)


@router.delete(
    "/{project_id}",
    response_model=ProjectDeleteResponse,
    summary="Удалить проект",
    description="""Удаляем проект по его ID""",
)
def delete_project(path: ProjectPath = Depends()):
    return ProjectDeleteResponse(id=1, project_id=path.project_id)


@router.patch(
    "/{project_id}",
    response_model=ProjectUpdateResponse,
    summary="Обновить проект",
    description="""Обновляем проект по его ID""",
)
def update_project(data: ProjectUpdateRequest, path: ProjectPath = Depends()):
    return ProjectUpdateResponse(
        id=path.project_id, key="123", name=data.name, description=data.description
    )


@router.post(
    "/",
    response_model=ProjectCreateResponse,
    status_code=HTTPStatus.CREATED,
    summary="Создать проект",
    description="""Создание нового проекта""",
)
async def create_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id=1, name=data.name)
