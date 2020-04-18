from fastapi import APIRouter, File, UploadFile
from datetime import datetime as dt
import crud

router = APIRouter()


@router.get("/")
async def read_root():
    return "Hello world!"


@router.get("/gallery")
async def results():
    imgs = crud.get_images()
    return imgs


@router.post("/gallery")
async def create_upload_file(name: str, category: str, upload_file: UploadFile = File(...)):
    # make unique name for each image - current time of posting
    path = 'images/' + dt.now().strftime("%d_%m_%Y_%H-%M-%S") + '.jpg'
    return crud.save_image(name, category, path, upload_file.file)


@router.get("/gallery/{id}")
async def results(id):
    img = crud.get_image_desc(id)
    return img


@router.get("/image/{id}")
async def results(id):
    img = crud.get_image(id)
    return img


@router.get("/gallery/category/{cat}")
async def results(cat: str):
    imgs = crud.get_images_cat(cat)
    return imgs
