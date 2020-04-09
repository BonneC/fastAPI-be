from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from starlette.responses import FileResponse

from config import DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base

from models import Base, ImgInfo

import shutil
from pathlib import Path
import datetime

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def append_image_to_data(imgs):
    json_imgs = jsonable_encoder(imgs)
    for img in json_imgs:
        img.update({'img': FileResponse(img['location'], media_type="image/jpg")})

    return json_imgs


# get all images from database
def get_images():
    with session_scope() as s:
        imgs = s.query(ImgInfo).all()
        # json_imgs = jsonable_encoder(imgs)
        return append_image_to_data(imgs)
        # for img in json_imgs:
        #     img.update({'img': FileResponse(img['location'], media_type="image/jpg")})
        # return json_imgs


# save image in db and file system
def save_image(name: str, category: str, path: str, file):
    path = Path(path)
    img = ImgInfo(name, path, category, datetime.date.today())

    with session_scope() as s:
        try:
            with path.open("wb") as buffer:
                shutil.copyfileobj(file, buffer)

            s.add(img)
            s.commit()

        finally:
            file.close()

        return 201, {"status": "sukses"}


# get image with ID
def get_image(id):
    with session_scope() as s:
        img = s.query(ImgInfo).get(id)
        # print(json)
        # json_img = jsonable_encoder(img)
        # json_img.update({'img': FileResponse(json_img['location'], media_type="image/jpg")})
        return append_image_to_data({img})


def get_images_cat(category):
    with session_scope() as s:
        imgs = s.query(ImgInfo).filter_by(category=category).all()
        return append_image_to_data(imgs)
