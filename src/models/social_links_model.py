from pydantic import BaseModel


class SocialLinkIn(BaseModel):
    child: str
    href: str
    style: str
    download: bool = False


class SocialLinkOut(SocialLinkIn):
    id: str
