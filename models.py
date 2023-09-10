from sqlalchemy import Integer, String, Column
from database import Base


class Book(Base):
    __tablename__='books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable="False")
    author = Column(String, nullable="False")
    publisher = Column(String, nullable="False")

