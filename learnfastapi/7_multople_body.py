from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# % curl -X 'PUT' \
#   'http://localhost:8000/items/123' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "item": {
#     "name": "pen",
#     "description": "a writing tool",
#     "price": 100,
#     "tax": 10
#   },
#   "user": {
#     "username": "Tom",
#     "full_name": "TomTom"
#   }
# }'
# {"item_id":123,"item":{"name":"pen","description":"a writing tool","price":100.0,"tax":10.0},"user":{"username":"Tom","full_name":"TomTom"}}%
