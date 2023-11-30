
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .routers.helloworld import helloworld_router
# import product router
from .routers.products import product_router

app = FastAPI(
    title="Product API",
    description="A simple API to demonstrate FastAPI",
    version="0.0.1",
    docs_url="/",
)

app.router.prefix = "/v1"

app.router.default_response_class = JSONResponse

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(product_router)
app.include_router(helloworld_router)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("product_api.main:app", host="0.0.0.0", port=5000, reload=True)


if __name__ == "__main__":
    start()
