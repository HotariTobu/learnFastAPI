from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

type Q = Annotated[str | None, Query(min_length=5)]


@app.get("/1/items")
async def read_items_1(q: Q = None):
    items = [{"item_id": "Foo"}, {"item_id": "Bar"}]
    if q:
        return {"items": items, "q": q}
    else:
        return {"items": items}


# % curl localhost:8000/1/items
# {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}%
# % curl localhost:8000/1/items\?q=foo
# {"detail":[{"type":"string_too_short","loc":["query","q"],"msg":"String should have at least 5 characters","input":"foo","ctx":{"min_length":5}}]}%
# % curl localhost:8000/1/items\?q=foobar
# {"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"foobar"}%


@app.get("/2/items")
async def read_items_2(q: Q = ...):
    items = [{"item_id": "Foo"}, {"item_id": "Bar"}]
    if q:
        return {"items": items, "q": q}
    else:
        return {"items": items}

# % curl localhost:8000/2/items
# {"detail":[{"type":"missing","loc":["query","q"],"msg":"Field required","input":null}]}%
# % curl localhost:8000/2/items\?q=foo
# {"detail":[{"type":"string_too_short","loc":["query","q"],"msg":"String should have at least 5 characters","input":"foo","ctx":{"min_length":5}}]}%
# % curl localhost:8000/2/items\?q=foobar
# {"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"q":"foobar"}%
