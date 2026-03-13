import os
from fastapi import FastAPI
import uvicorn
from debug.routes import router as debug_router
from dotenv import load_dotenv

from config import HTTP_LISTEN_HOST, HTTP_LISTEN_PORT

load_dotenv()

app = FastAPI()
app.include_router(debug_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=HTTP_LISTEN_HOST, port=int(HTTP_LISTEN_PORT))
