from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class ImgInfo(Base):
    __tablename__ = 'img_info'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    location = Column(String)
    category = Column(String)
    created = Column(Date)

    def __repr__(self):
        return "<Image(title='{}', location='{}', category={}, created={})>" \
            .format(self.title, self.location, self.category, self.created)
