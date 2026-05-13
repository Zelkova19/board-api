from fastapi import FastAPI

from app.projects.routes import router as projects_router
from app.tasks.routes import router as tasks_router

app = FastAPI(
    title="KanbanBoard API",
    version="0.0.1",
    description="API для работы приложения-аналога Jira",
    openapi_tags=[
        {"name": "Projects", "description": "Управление проектом"},
        {"name": "Tasks", "description": "Управление задачами"},
    ],
)

app.include_router(projects_router)
app.include_router(tasks_router)
