import os

from fastapi import APIRouter, FastAPI, File, UploadFile
from models import ImgInfo
from crud import engine, Session
import datetime
from datetime import datetime as dt
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
import crud

router = APIRouter()
s = Session()


@router.get("/")
async def read_root():
    return "Hello world!"


@router.get("/gallery")
async def results():
    imgs = crud.get_images()
    return imgs


@router.post("/gallery")
async def create_upload_file(name: str, category: str, upload_file: UploadFile = File(...)):
    path = 'images/' + dt.now().strftime("%d_%m_%Y_%H-%M-%S") + '.jpg'
    return crud.save_image(name, category, path, upload_file.file)


@router.get("/gallery/{id}")
async def results(id):
    img = crud.get_image(id)
    return img


@router.get("/gallery/category/{cat}")
async def results(cat: str):
    res = s.query(ImgInfo).filter_by(category=cat).all()
    imgs = crud.get_images_cat(cat)
    return imgs
