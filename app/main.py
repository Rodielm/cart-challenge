
from fastapi import Depends, FastAPI, Header, HTTPException
import uvicorn
from app.core import config
from starlette.middleware.cors import CORSMiddleware
from app.api.api import router as api_router
from app.db.settings import init

app = FastAPI(config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

origins = [
    "http://localhost:8080",
    "http://localhost:8888",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", init)
app.include_router(api_router, prefix="/api/v1")
