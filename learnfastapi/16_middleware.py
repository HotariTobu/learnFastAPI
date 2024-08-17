import asyncio
import time
from typing import Callable, Coroutine

from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(
    request: Request, call_next: Callable[[Request], Coroutine[None, None, Response]]
):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/items")
async def read_items():
    await asyncio.sleep(0.5)
    return {"items": []}


# % curl -v localhost:8000/items
# * Host localhost:8000 was resolved.
# * IPv6: ::1
# * IPv4: 127.0.0.1
# *   Trying [::1]:8000...
# * connect to ::1 port 8000 from ::1 port 55065 failed: Connection refused
# *   Trying 127.0.0.1:8000...
# * Connected to localhost (127.0.0.1) port 8000
# > GET /items HTTP/1.1
# > Host: localhost:8000
# > User-Agent: curl/8.6.0
# > Accept: */*
# >
# < HTTP/1.1 200 OK
# < date: Sat, 17 Aug 2024 01:30:23 GMT
# < server: uvicorn
# < content-length: 12
# < content-type: application/json
# < x-process-time: 0.5116369724273682
# <
# * Connection #0 to host localhost left intact
# {"items":[]}%
