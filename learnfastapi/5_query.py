from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# % curl localhost:8000/items/foo
# {"item_id":"foo","description":"This is an amazing item that has a long description"}%
# % curl localhost:8000/items/foo\?q=bar
# {"item_id":"foo","q":"bar","description":"This is an amazing item that has a long description"}%
# % curl localhost:8000/items/foo\?q=bar\&short=0
# {"item_id":"foo","q":"bar","description":"This is an amazing item that has a long description"}%
# % curl localhost:8000/items/foo\?q=bar\&short=1
# {"item_id":"foo","q":"bar"}%
# % curl localhost:8000/items/foo\?q=bar\&short=true
# {"item_id":"foo","q":"bar"}%
# % curl localhost:8000/items/foo\?q=bar\&short=false
# {"item_id":"foo","q":"bar","description":"This is an amazing item that has a long description"}%
# % curl localhost:8000/items/foo\?q=bar\&short=on
# {"item_id":"foo","q":"bar"}%
# % curl localhost:8000/items/foo\?q=bar\&short=off
# {"item_id":"foo","q":"bar","description":"This is an amazing item that has a long description"}%
# % curl localhost:8000/items/foo\?q=bar\&short=yes
# {"item_id":"foo","q":"bar"}%
# % curl localhost:8000/items/foo\?q=bar\&short=no
# {"item_id":"foo","q":"bar","description":"This is an amazing item that has a long description"}%
