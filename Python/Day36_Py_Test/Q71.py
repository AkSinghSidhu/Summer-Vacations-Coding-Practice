# Set up a FastAPI app. Create endpoints: `GET /` returns a welcome message, `GET /items` returns a list of hardcoded items, `GET /items/{item_id}` returns one item or 404. Run with `uvicorn` and explore the auto-generated Swagger docs at `/docs`.

from fastapi import FastAPI, HTTPException

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
def add_items(item: dict):

    if "name" not in item:
        raise HTTPException(
            status_code = 400,
            detail = "Name is Required"
        )
    
    if "price" not in item:
        raise HTTPException(
            status_code = 400,
            detail = "Price is required"
        )
    
    if "stock" not in item:
        raise HTTPException(
            status_code = 400,
            detail = "Stock is required"
        )
    
    if "category" not in item:
        raise HTTPException(
            status_code = 400,
            detail = "Category is Required"
        )
    
    if not isinstance(item["name"], str):
        raise HTTPException(
            status_code = 400,
            detail = "Name must be String"
        )
    
    if not isinstance(item["price"], int):
        raise HTTPException(
            status_code = 400,
            detail = "Price must be Integer"
        )
    
    if not isinstance(item["stock"], int):
        raise HTTPException(
            status_code = 400,
            detail = "Stock must be Integer"
        )
    
    if not isinstance(item["category"], str):
        raise HTTPException(
            status_code = 400,
            detail = "Category must be String"
        )
    

    new_id = len(items) + 1
    items[new_id] = item
    return {
        "id": new_id,
        "item": items[new_id]
    }