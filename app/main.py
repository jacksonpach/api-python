from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api import user_routes

app = FastAPI()


@app.get("/health")
async def health():
    return JSONResponse(status_code=200, content={"status": "ok"})


app.include_router(user_routes.router)

