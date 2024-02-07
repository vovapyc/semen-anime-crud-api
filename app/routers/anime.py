from models import AnimeModel
from fastapi import HTTPException, APIRouter
import time
from pydantic import BaseModel
from typing import List


class BaseAnime(BaseModel):
    name: str
    main_genre: str
    year: int
    poster_link: str

    rating: str
    review: str


class CreateAnime(BaseAnime):
    pass


class Anime(BaseAnime):
    id: int
    created_at: int
    updated_at: int


router = APIRouter()


@router.post("/", response_model=Anime)
async def create_anime(anime: CreateAnime):
    anime_data = anime.model_dump()

    current_time = int(time.time())
    anime_data["created_at"] = current_time
    anime_data["updated_at"] = current_time

    anime_model = AnimeModel.create(**anime_data)
    return anime_model


@router.get("", response_model=List[Anime])
async def get_all_anime():
    return list(AnimeModel.select())


@router.get("/{anime_id}", response_model=Anime)
async def get_anime(anime_id: int):
    try:
        anime_model = AnimeModel.get(AnimeModel.id == anime_id)
        return anime_model
    except AnimeModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Anime not found")


@router.put("/{anime_id}", response_model=Anime)
async def update_anime(anime_id: int, anime: CreateAnime):
    try:
        anime_model = AnimeModel.get(AnimeModel.id == anime_id)
        anime_data = anime.dict()
        for key, value in anime_data.items():
            setattr(anime_model, key, value)
        anime_model.save()
        return anime_model
    except AnimeModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Anime not found")


@router.delete("/{anime_id}", response_model=Anime)
async def delete_anime(anime_id: int):
    try:
        anime_model = AnimeModel.get(AnimeModel.id == anime_id)
        anime_model.delete_instance()
        return anime_model
    except AnimeModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Anime not found")
