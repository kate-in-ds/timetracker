from fastapi import FastAPI
from .routers import activities

app = FastAPI(title="TimeTrack Analytics API")

# подключаем роутеры
app.include_router(activities.router)

@app.get("/")
def root():
    return {"message": "Backend works"}