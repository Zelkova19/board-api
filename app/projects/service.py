import logging
from typing import Annotated

from fastapi import Depends

from .repository import ProjectRepository, ProjectRepositoryDeps

logger = logging.getLogger(__name__)


def get_project_service(repo: ProjectRepositoryDeps):
    return ProjectService(repo)


class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def get_project(self, project_id: int):
        try:
            return self.repo.get_by_id(project_id)
        except ValueError as e:
            logger.error("Ошибка %s", e, exc_info=True)


ProjectServiceDeps = Annotated[ProjectService, Depends(get_project_service)]
