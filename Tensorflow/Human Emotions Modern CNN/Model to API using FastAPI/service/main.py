# ONNX RUNTIME AND OPENCV HAS TO BE INSTALLE BEFORE WE CAN USE THIS CODES, WE HAVE TO BE IN A VIRTUAL ENRIRONMENT BEFORE WE CAN INSTALL THEm

from fastapi import FastAPI
from service.api.api import main_router

app = FastAPI(project_name="emotions Detection")
app.include_router(main_router)
app.get('/')


def root():
    return {'hello': 'world'}


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
