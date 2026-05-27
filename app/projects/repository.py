from typing import Annotated

from fastapi import Depends


def get_project_repository():
    return ProjectRepository()


class ProjectRepository:
    def get_by_id(self, project_id: int):
        if project_id > 100:
            raise ValueError("Больше 100")
        return project_id


ProjectRepositoryDeps = Annotated[ProjectRepository, Depends(get_project_repository)]
