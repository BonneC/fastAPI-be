import shutil
from pathlib import Path
import datetime
import os

from fastapi.encoders import jsonable_encoder
from starlette.responses import FileResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from config import DATABASE_URI
from models import ImgInfo

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


# put image and image information from database into a json
def append_image_to_data(imgs):
    json_imgs = jsonable_encoder(imgs)
    for img in json_imgs:
        img.update({'img': FileResponse(img['location'], media_type="image/jpg")})

    return json_imgs


# get all images from database
def get_images():
    with session_scope() as s:
        imgs = s.query(ImgInfo).all()
        json_imgs = jsonable_encoder(imgs)
        return json_imgs


# save image in db and file system
def save_image(name: str, category: str, path: str, file):
    p = Path(path)
    img = ImgInfo(name, path, category, datetime.date.today())

    with session_scope() as s:
        try:
            with p.open("wb") as buffer:
                shutil.copyfileobj(file, buffer)

            s.add(img)
            s.commit()

        finally:
            file.close()

        return 201, {"status": "sukses"}


def update_image(id, name: str, category: str):
    with session_scope() as s:
        img = s.query(ImgInfo).get(id)
        img.title = name
        img.category = category
        s.commit()

    return 201, {"status": "sukses"}


# get img info from database
def get_image_desc(id):
    with session_scope() as s:
        img = s.query(ImgInfo).get(id)
        return jsonable_encoder(img)


# get image with ID
def get_image(id):
    with session_scope() as s:
        img = s.query(ImgInfo).get(id)
        return FileResponse(img.location, media_type="image/jpg")


def delete_image(id):
    with session_scope() as s:
        img = s.query(ImgInfo).get(id)
        path = img.location
        s.delete(img)
        s.commit()
        try:
            os.remove(path)
        except Exception as e:
            print(e)
            return 500, {"status": "oopsie"}
    return 201, {"status": "sukses"}


# get all images from category
def get_images_cat(category):
    with session_scope() as s:
        imgs = s.query(ImgInfo).filter_by(category=category).all()
        return jsonable_encoder(imgs)
