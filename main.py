from fastapi import FastAPI, Depends
from schema import BookSchema
from models import Base, Book
from database import engine, get_db
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def index():
    return f"Hello"

@app.get("/books")
def get_all(db: Session=Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{id1}")
def get_id(id1: int, db: Session=Depends(get_db)):
    get_book=db.query(Book).filter(Book.id==id1).first()
    if get_book is not None:
        return  get_book
    else:
        return f"not found!"

@app.post("/books")
def insert_book(schema1: BookSchema, db: Session=Depends(get_db)):
    book_model=Book(**schema1.dict())
    db.add(book_model)
    db.commit()
    return {"book added": book_model.title}


@app.delete("/books/{id1}")
def delete_book(id1: int, db: Session=Depends(get_db)):
    get_book=db.query(Book).filter(Book.id==id1).first()

    if get_book is None:
        return f"not found!"
    else:
        db.delete(get_book)
        db.commit()
    return f"no content!"

@app.put("/books/{id1}")
def updated_book(id1: int, schema1: BookSchema, db: Session=Depends(get_db)):
    get_book=db.query(Book).filter(Book.id==id1).first()

    if get_book is None:
        return f"not found!"
    else:
        get_book.title=schema1.title
        get_book.author=schema1.author
        get_book.publisher=schema1.publisher
        db.commit()
        db.refresh(get_book)
        return f"successful updated!"
    return f"no content!"





