from fastapi import FastAPI

from app.post.routes import router as post_router

app = FastAPI()

app.include_router(post_router)
