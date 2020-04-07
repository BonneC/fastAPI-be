import os

from fastapi import APIRouter, FastAPI, File, UploadFile
from models import ImgInfo
from crud import engine, Session
import datetime
from datetime import datetime as dt
import shutil
from pathlib import Path
from fastapi.responses import FileResponse

router = APIRouter()
s = Session()


@router.get("/")
async def read_root():
    imgs = s.query(ImgInfo).all()
    s.close()
    return imgs


@router.get("/gallery")
async def results():
    res = s.query(ImgInfo).all()
    return res


@router.post("/gallery")
async def create_upload_file(upload_file: UploadFile = File(...)):
    imazh = 'images/' + dt.now().strftime("%d_%m_%Y_%H-%M-%S") + '.jpg'
    img = ImgInfo('actual_imazh', imazh, 'cat1', datetime.date.today())
    # {'title': 'actual_imazh', 'location': imazh, 'category': 'cat1', 'created': datetime.date.today()}
    path = Path(imazh)
    try:
        with path.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        s.add(img)
        s.commit()

    finally:
        upload_file.file.close()

    return 201, {"status": "sukses"}


@router.get("/gallery/{id}")
async def results(id):
    res = s.query(ImgInfo).get(id)
    img = open(res.location, 'r')
    return FileResponse(res.location, media_type="image/jpg")
    #return res


@router.get("/gallery/category/{cat}")
async def results(cat: str):
    res = s.query(ImgInfo).filter_by(category=cat).all()
    return res
