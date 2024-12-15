from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()


class ItemC(BaseModel):
    name: str = None
    id_done: bool = False
    validated_not_null: bool
    
items = []

@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: ItemC):
    items.append(item)
    return items

@app.get("/items/{item_id}", response_model = ItemC)
def get_item(item_id: int) -> ItemC:
    if item_id < len(items):
        item = items[item_id]
        return  items[item_id]
    else:
        raise HTTPException(status_code=404, detail ="No Such Item")

@app.get("/items", response_model = list[ItemC])
def list_items(limit: int =2):
    return items[0:limit]

    