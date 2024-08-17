from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/items")
def read_items():
    raise Exception("Some error")


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    raise HTTPException(status_code=404, detail="Item not found")


# % curl localhost:8000/items
# Internal Server Error%

# % curl localhost:8000/items/foo
# {"detail":"Item not found"}%
