from fastapi import FastAPI

from .routers import items, users

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# % curl localhost:8000/users
# [{"username":"Rick"},{"username":"Morty"}]%
# % curl localhost:8000/users/me
# {"username":"fakecurrentuser"}%
# % curl localhost:8000/users/foo
# {"username":"foo"}%s

# % curl localhost:8000/items
# {"plumbus":{"name":"Plumbus"},"gun":{"name":"Portal Gun"}}%
# % curl localhost:8000/items/plumbus
# {"name":"Plumbus","item_id":"plumbus"}%
# % curl localhost:8000/items/foo
# {"detail":"Item not found"}%
# % curl -X PUT localhost:8000/items/plumbus
# {"item_id":"plumbus","name":"The great Plumbus"}%
# % curl -X PUT localhost:8000/items/gun
# {"detail":"You can only update the item: plumbus"}%
# % curl -X PUT localhost:8000/items/foo
# {"detail":"You can only update the item: plumbus"}%
# %
