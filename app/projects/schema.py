from fastapi import HTTPException
from pydantic import BaseModel, field_validator, Field


class ProjectPath(BaseModel):
    project_id: int = Field(gt=0)


class ProjectGetResponse(BaseModel):
    id: int
    project_id: int


class ProjectDeleteResponse(BaseModel):
    id: int
    project_id: int


class ProjectUpdateRequest(BaseModel):
    name: str | None = None
    description: str | None = None


class ProjectUpdateResponse(BaseModel):
    id: int
    key: str
    name: str | None = None
    description: str | None = None


class ProjectCreateRequest(BaseModel):
    key: str
    name: str
    description: str | None = None

    model_config = {"extra": "ignore"}

    @field_validator("key")
    @classmethod
    def key_not_empty(cls, value):
        value = value.strip()
        if not value:
            raise HTTPException(400, "key must be valid string")
        return value


class ProjectCreateResponse(BaseModel):
    id: int
    name: str
