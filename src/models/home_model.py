from pydantic import BaseModel


class HomeIn(BaseModel):
    title: str
    message: str
    description: str
    profile_image: str


class HomeOut(HomeIn):
    id: str