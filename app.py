
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import starlette.status as statusCode

import asyncio


app = FastAPI(title="NASA 2021")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



from fastapi import APIRouter
router = APIRouter()


from pydantic import BaseModel
from datetime import datetime
import random
import json


from fastapi.responses import HTMLResponse, FileResponse
import os

from api.point_calculator import router as point_calculator_router

app.include_router(point_calculator_router, prefix="", tags=["API"])

from db import db


static_file_path = "./static/"
@app.get("/")
def home():
    with open(f"{static_file_path}/index.html") as f:
        html = "".join(f.readlines())
    return HTMLResponse(content=html, status_code= 200)

@app.get("/{whatever:path}")
async def get_static_files_or_404(whatever):
    # try open file for path
    file_path = os.path.join(static_file_path,whatever)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse(f"{static_file_path}/index.html")


if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=14001)

