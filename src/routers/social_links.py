from typing import List

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from src.config.database import db
from src.models.social_links_model import SocialLinkIn, SocialLinkOut

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


@router.post("", response_model=SocialLinkOut, status_code=status.HTTP_201_CREATED, )
def create_social_link(social_link: SocialLinkIn):
    result = social_links_collection.insert_one(social_link.dict())
    created = social_links_collection.find_one({"_id": ObjectId(result.inserted_id)})
    if not created:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create social link",
        )
    return serialize_social_link(created)

@router.delete("/{social_link_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_social_link(social_link_id: str):
    result = social_links_collection.delete_one({"_id": ObjectId(social_link_id)})
    print(result)
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Social link not found",
        )
    return None

@router.put("/{social_link_id}", response_model=SocialLinkOut, status_code=status.HTTP_200_OK)
def update_social_link(social_link_id: str, social_link: SocialLinkIn):
    result = social_links_collection.find_one_and_update(
        {"_id": ObjectId(social_link_id)},
        {"$set": social_link.dict()},
        return_document=True
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Social link not found",
        )
    return serialize_social_link(result)