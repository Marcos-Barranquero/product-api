import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models.product import Product
from .data.products import products

# import product router
from .routers.products import product_router
from .routers.helloworld import helloworld_router

from dataclasses import dataclass

app = FastAPI()

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
