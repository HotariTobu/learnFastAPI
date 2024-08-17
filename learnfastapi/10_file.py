from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# % curl -X 'POST' \
#   'http://localhost:8000/files' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F "file=@./pyproject.toml"
# {"file_size":330}%

#% curl -X 'POST' \
#   'http://localhost:8000/uploadfile' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F "file=@./pyproject.toml"
# {"filename":"pyproject.toml"}%
