# Convert your FastAPI item endpoints to async. Add a `GET /items/search` endpoint that accepts a query parameter `?keyword=xyz` and filters items by name. Add a `PUT /items/{item_id}` to update an item and `DELETE /items/{item_id}` to remove one. Use an in-memory list as your data store.

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
async def home():
    return {"message": "Welcome"}

@app.get("/items")
async def get_items():
    return items

@app.get("/items/search")
async def search(keyword: str):
    filtered = []
    for id, info in items.items():
        if keyword.lower() in info["name"].lower():
            filtered.append(info)

    if not filtered:
        raise HTTPException(
            status_code = 404,
            detail = "Item not found"
        )
    else:
        return filtered

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code = 404,
            detail = "Item not found"
        )
    
    return items[item_id]

@app.put("/items/{item_id}", status_code = 200)
async def put_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(
            status_code = 404,
            detail = "Item not found"
        )
    
    items[item_id] = {
        "name": item.name,
        "price": item.price,
        "stock": item.stock,
        "category": item.category
    }

    return {
        "id": item_id,
        "item": items[item_id]
    }

@app.delete("/items/{item_id}", status_code = 200)
async def del_items(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code = 404,
            detail = "Item not found"
        )
    items.pop(item_id)
    return {
    "message": "Item deleted successfully"
    }

@app.post("/items", status_code = 201)
async def add_items(item: Item):
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
