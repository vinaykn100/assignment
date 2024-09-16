import os, sys
from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.api_v1.api import router as api_router
from mangum import Mangum
import uvicorn


app = FastAPI()
app.include_router(api_router, prefix="/api/v1")

handler = Mangum(app, lifespan="off", api_gateway_base_path='/')


if __name__ == "__main__":
    uvicorn.run("app.main:app", host='localhost', port=8000, reload=True)