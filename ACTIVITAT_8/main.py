from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

items = {
    1: {"id": 1, "name": "xavi", "age": 19, "gender": "male", "weight": 68.5, "height": 1.66},
}

class Item(BaseModel):
    id: int
    name: str
    age: int
    gender: Optional[str] = None
    weight: float
    height: float
    
@app.get("/items/{item_id}")
def get_item(item_id: int, response: Response):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"Item id": item_id}

@app.post("/items/")
def create_item(item: Item):
    
    return {
        "Item id": item.id,
        "Item name": item.name,
        "Item age": item.age,
        "Description": item.gender,
        "Price": item.weight,
        "In stock": item.height
    }