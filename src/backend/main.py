from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/backend/static"), name="static")

@app.get("/")
def testing():
    return {"Penis": "Balls"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("src/backend/static/favicon.ico")


