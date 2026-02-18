from fastapi import FastAPI

from src.routers.social_links import router as social_links_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


app.include_router(social_links_router, prefix="/social-links", tags=["social-links"])