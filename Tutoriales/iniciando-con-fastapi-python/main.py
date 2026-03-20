from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hola, Mundo!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"fake_items_db": [{"item_name": "Foo"}, {"item_name": "Bar"}]}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}
