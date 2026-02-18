from typing import List

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from config.database import db
from models.social_links_model import SocialLinkIn, SocialLinkOut

router = APIRouter()

social_links_collection = db["social_links"]


def serialize_social_link(doc: dict) -> dict:
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


@router.get("", response_model=List[SocialLinkOut])
def get_social_links():
    docs = list(social_links_collection.find())
    return [serialize_social_link(doc) for doc in docs]


@router.post("", response_model=SocialLinkOut, status_code=status.HTTP_201_CREATED)
def create_social_link(social_link: SocialLinkIn):
    result = social_links_collection.insert_one(social_link.dict())
    created = social_links_collection.find_one({"_id": ObjectId(result.inserted_id)})
    if not created:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create social link",
        )
    return serialize_social_link(created)
