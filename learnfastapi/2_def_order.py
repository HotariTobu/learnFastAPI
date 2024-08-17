from fastapi import FastAPI

app = FastAPI()


@app.get("/1/users/me")
def read_user_me_1():
    return {"user": "me"}


@app.get("/1/users/{user_id}")
def read_user_str_1(user_id: str):
    return {"user_id": user_id}


# % curl localhost:8000/1/users/me
# {"user":"me"}%
# % curl localhost:8000/1/users/5
# {"user_id":"5"}%
# % curl localhost:8000/1/users/foo
# {"user_id":"foo"}%


###


@app.get("/2/users/me")
def read_user_me_2():
    return {"user": "me"}


@app.get("/2/users/{user_id}")
def read_user_int_2(user_id: int):
    return {"user_id": user_id}


@app.get("/2/users/{user_id}")
def read_user_str_2(user_id: str):
    return {"user_id": user_id}


# % curl localhost:8000/2/users/me
# {"user":"me"}%
# % curl localhost:8000/2/users/5
# {"user_id":5}%
# % curl localhost:8000/2/users/foo
# {"detail":[{"type":"int_parsing","loc":["path","user_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"foo"}]}%


###


@app.get("/3/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/3/users")
async def read_users2():
    return ["Bean", "Elfo"]


# % curl localhost:8000/3/users
# ["Rick","Morty"]%
