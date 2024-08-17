from enum import StrEnum, auto

from fastapi import FastAPI


class ModelName(StrEnum):
    ALEXNET = auto()
    RESNET = auto()
    LENET = auto()


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name == ModelName.LENET:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# % curl localhost:8000/models/alexnet
# {"model_name":"alexnet","message":"Deep Learning FTW!"}%
# % curl localhost:8000/models/resnet
# {"model_name":"resnet","message":"Have some residuals"}%
# % curl localhost:8000/models/lenet
# {"model_name":"lenet","message":"LeCNN all the images"}%
# % curl localhost:8000/models/foo
# {"detail":[{"type":"enum","loc":["path","model_name"],"msg":"Input should be 'alexnet', 'resnet' or 'lenet'","input":"foo","ctx":{"expected":"'alexnet', 'resnet' or 'lenet'"}}]}%
