from fastapi import FastAPI
from crud import engine, Session
from models import Base, ImgInfo

app = FastAPI()
# Base.metadata.create_all(engine)
s = Session()


@app.get("/")
def read_root():
    imgs = s.query(ImgInfo).all()
    s.close()
    return imgs


@app.get("/gallery/{id}")
def results(id):
    res = s.query(ImgInfo).get(id)
    return res


@app.get("/gallery/category/{cat}")
def results(cat: str):
    res = s.query(ImgInfo).filter_by(category=cat).all()
    return res

# @app.post("/my_stash")
# async def create_item(item: Item):
#     return item
