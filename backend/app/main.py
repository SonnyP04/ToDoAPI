from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import todos

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
)

app.include_router(todos.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

