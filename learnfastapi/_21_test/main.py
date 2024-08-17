from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


# % pytest
# ================================================================= test session starts ==================================================================
# platform darwin -- Python 3.12.3, pytest-8.3.2, pluggy-1.5.0
# rootdir: /path/to/learnFastAPI
# configfile: pyproject.toml
# plugins: anyio-4.4.0
# collected 1 item

# learnfastapi/_21_test/main_test.py .                                                                                                             [100%]

# ================================================================== 1 passed in 0.32s ===================================================================
