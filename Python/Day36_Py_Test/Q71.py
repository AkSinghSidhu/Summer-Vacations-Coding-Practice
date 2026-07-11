# Set up a FastAPI app. Create endpoints: `GET /` returns a welcome message, `GET /items` returns a list of hardcoded items, `GET /items/{item_id}` returns one item or 404. Run with `uvicorn` and explore the auto-generated Swagger docs at `/docs`.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {
    1: {
        "name": "Laptop",
        "price": 75000,
        "stock": 15,
        "category": "Electronics"
    },
    2: {
        "name": "Wireless Mouse",
        "price": 1200,
        "stock": 50,
        "category": "Accessories"
    },
    3: {
        "name": "Mechanical Keyboard",
        "price": 4500,
        "stock": 20,
        "category": "Accessories"
    },
    4: {
        "name": "Monitor",
        "price": 18000,
        "stock": 10,
        "category": "Electronics"
    },
    5: {
        "name": "USB-C Cable",
        "price": 500,
        "stock": 100,
        "category": "Cables"
    }
}

class Item(BaseModel):
    name: str
    price: int
    stock: int
    category: str

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code = 404,
            detail = "Item not found"
        )
    
    return items[item_id]

@app.post("/items", status_code = 201)
def add_items(item: Item):
    new_id = max(items.keys()) + 1
    items[new_id] = {
        "name": item.name,
        "price": item.price,
        "stock": item.stock,
        "category": item.category
    }

    return {
        "id": new_id,
        "item": items[new_id]
    }