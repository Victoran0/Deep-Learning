# ONNX RUNTIME AND OPENCV HAS TO BE INSTALLE BEFORE WE CAN USE THIS CODES, WE HAVE TO BE IN A VIRTUAL ENRIRONMENT BEFORE WE CAN INSTALL THEm

import onnxruntime as rt
from fastapi import FastAPI
from service.api.api import main_router

app = FastAPI(project_name="emotions Detection")
app.include_router(main_router)

providers = ['CPUExecutionProvider']
m_q = rt.InferenceSession(
    "eff_quantized.onnx", providers=providers)


@app.get('/')
async def root():
    return {'hello': 'world'}


# The advantage of fastapi is that we can run our functions asynchronously. But in some CPU bound task such as Computer Vision, object detection, deep learning etc, async functions would not help us speed up time taken to run because they still have no run completely. In this case, we would make use of parrallelism. In parallelism, instead of having one CPU worker to run all the different tasks, we can allocate 3 workers, where each worker can focus on a given task. TO do this, we can simply use Gunicorn


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class InputItem(BaseModel):
#     name: str
#     price: int
#     discount: int


# class OutputItem(BaseModel):
#     name: str
#     selling_price: int


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.post("/items/", response_model=OutputItem)
# def add_item(item: InputItem):
#     selling_price = item.price - item.discount
#     return {"name": item.name, "selling_price": selling_price}
