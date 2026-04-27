from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"scoup": 10}
