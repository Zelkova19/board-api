from fastapi import FastAPI

from app.projects.routes import router as projects_router

app = FastAPI(
    title="KanbanBoard API",
    version="0.0.1",
    description="API для работы приложения-аналога Jira",
    openapi_tags=[{"name": "Projects", "description": "Управление проектом"}],
)

app.include_router(projects_router)
