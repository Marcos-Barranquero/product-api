from fastapi import APIRouter

helloworld_router = APIRouter()


@helloworld_router.get("/")
def message():
  return "Hello, world! I'm a FastAPI app!"


@helloworld_router.get("/goodbye")
def goodbye():
  return "Goodbye, world!"
