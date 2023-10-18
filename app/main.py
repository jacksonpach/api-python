from decouple import config
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.config import settings
from app.config.config_debug import setup_debugger
from app.routes import user_routes

app = FastAPI()

if settings.DEBUG:
    app.add_event_handler("startup", setup_debugger)


@app.get("/health")
async def health():
    return JSONResponse(status_code=200, content={"status": "ok"})


app.include_router(user_routes.router)
