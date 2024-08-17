from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


# % curl -X 'POST' \
#   'http://localhost:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "pen",
#   "description": "a writing tool",
#   "price": 100,
#   "tax": 10,
#   "tags": ["write", "draw"]
# }'
# {"name":"pen","description":"a writing tool","price":100.0,"tax":10.0,"tags":["write","draw"]}%

# % curl localhost:8000/items
# [{"name":"Portal Gun","description":null,"price":42.0,"tax":null,"tags":[]},{"name":"Plumbus","description":null,"price":32.0,"tax":null,"tags":[]}]%


###


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserOut):
    password: str


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# % curl -X 'POST' \
#   'http://localhost:8000/user/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "username": "Tom",
#   "password": "Mot",
#   "email": "tom@example.com",
#   "full_name": "TomTom"
# }'
# {"username":"Tom","email":"tom@example.com","full_name":"TomTom"}%
