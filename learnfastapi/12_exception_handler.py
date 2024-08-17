from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"user_id": user_id}


# % curl localhost:8000/users/5
# {"user_id":5}%
# % curl localhost:8000/users/3
# Nope! I don't like 3.%
# % curl localhost:8000/users/foo
# [{'type': 'int_parsing', 'loc': ('path', 'user_id'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'foo'}]%
