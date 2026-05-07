from fastapi import APIRouter, Depends
from .schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectDeleteResponse,
    ProjectGetResponse,
    ProjectPath,
    ProjectUpdateResponse,
    ProjectUpdateRequest,
)


router = APIRouter(prefix="/projects")


@router.get("/{project_id}", response_model=ProjectGetResponse)
def get_project(path: ProjectPath = Depends()):
    return ProjectGetResponse(id=1, project_id=path.project_id)


@router.delete("/{project_id}", response_model=ProjectDeleteResponse)
def delete_project(path: ProjectPath = Depends()):
    return ProjectDeleteResponse(id=1, project_id=path.project_id)


@router.patch("/{project_id}", response_model=ProjectUpdateResponse)
def update_project(data: ProjectUpdateRequest, path: ProjectPath = Depends()):
    return ProjectUpdateResponse(
        id=path.project_id, key="123", name=data.name, description=data.description
    )


@router.post("/", response_model=ProjectCreateResponse)
async def creat_project(data: ProjectCreateRequest):
    return ProjectCreateResponse(id=1, name=data.name)
