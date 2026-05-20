from fastapi import FastAPI

from app.core.settings import Settings
from app.projects.routes import router as projects_router
from app.tasks.routes import router as tasks_router


def create_app() -> FastAPI:
    settings = Settings()  # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app.name,
        version="0.0.1",
        description="API для работы приложения-аналога Jira",
        openapi_tags=[
            {"name": "Projects", "description": "Управление проектом"},
            {"name": "Tasks", "description": "Управление задачами"},
        ],
    )
    new_app.state.settings = settings

    new_app.include_router(projects_router)
    new_app.include_router(tasks_router)
    return new_app


app = create_app()
