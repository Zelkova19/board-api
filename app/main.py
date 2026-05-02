from fastapi import FastAPI

from app.post.routes import router as post_router
from app.rand.routes import router as rand_router

app = FastAPI()

app.include_router(post_router)
app.include_router(rand_router)
