from fastapi import FastAPI

from models import Base, ImgInfo
from api import router

app = FastAPI()
# Base.metadata.create_all(engine)


app.include_router(router.router)




# @app.post("/my_stash")
# async def create_item(item: Item):
#     return item
