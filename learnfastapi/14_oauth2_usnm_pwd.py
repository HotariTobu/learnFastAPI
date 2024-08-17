from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme_1 = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items")
async def read_items(token: Annotated[str, Depends(oauth2_scheme_1)]):
    return {"token": token}


# % curl localhost:8000/items \
# -u Tom:Mot
# {"detail":"Not authenticated"}%


###


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token_1(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user_1(token: Annotated[str, Depends(oauth2_scheme_1)]):
    user = fake_decode_token_1(token)
    return user


@app.get("/1/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user_1)]):
    return current_user


###


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme_2 = OAuth2PasswordBearer(tokenUrl="/2/token")


class UserInDB(User):
    hashed_password: str


def get_user_2(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token_2(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user_2(fake_users_db, token)
    return user


async def get_current_user_2(token: Annotated[str, Depends(oauth2_scheme_2)]):
    user = fake_decode_token_2(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user_2(
    current_user: Annotated[User, Depends(get_current_user_2)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/2/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/2/users/me")
async def read_users_me_2(
    current_user: Annotated[User, Depends(get_current_active_user_2)],
):
    return current_user


# % curl -X POST localhost:8000/2/token \
# -d username=johndoe \
# -d password=secret
# {"access_token":"johndoe","token_type":"bearer"}%
# % curl localhost:8000/2/users/me \
# -H "Authorization: Bearer johndoe"
# {"username":"johndoe","email":"johndoe@example.com","full_name":"John Doe","disabled":false,"hashed_password":"fakehashedsecret"}%
