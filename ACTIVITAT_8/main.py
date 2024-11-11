from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    age: int
    
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"Item id": item_id}

@app.post("/items/")
def create_item(item: Item):
    
    return {"Item id": item.id, "Item name": item.name, "Item age": item.age}