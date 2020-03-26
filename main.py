from fastapi import FastAPI
from crud import engine, Session
from models import Base, ImgInfo

app = FastAPI()
#Base.metadata.create_all(engine)
s = Session()


@app.get("/")
def read_root():
    img = s.query(ImgInfo).first()
    s.close()
    return {"Hello": img}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/gallery/graphs")
def results():
    #    results = some_library()
    return 1

@app.get("/gallery/drawings")
def results():
    #    results = some_library()
    return 1

# @app.post("/my_stash")
# async def create_item(item: Item):
#     return item