from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# % curl localhost:8000/files/foo.txt
# {"file_path":"foo.txt"}%
# % curl localhost:8000/files/foo/bar.txt
# {"file_path":"foo/bar.txt"}%
# % curl localhost:8000/files/foo/bar/buz.txt
# {"file_path":"foo/bar/buz.txt"}%
