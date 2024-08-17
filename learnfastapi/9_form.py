from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    print("password:", password)
    return {"username": username}


# % curl -X 'POST' \
#   'http://localhost:8000/login' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/x-www-form-urlencoded' \
#   -d 'username=Tom&password=Mot'
# {"username":"Tom"}%
