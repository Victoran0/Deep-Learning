from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
import numpy as np
from service.core.logic.onnx_inference import emotions_detector

emo_router = APIRouter()


@detect_router.post('detect/')
def emo_router(im: UploadFile):

    if im.filename.split('.')[-1] in ('jpg', 'jpeg', 'png'):
        pass
    else:
        raise HTTPException(
            status_code=415, detail="Not an image")

    image = Image.open(BytesIO(im.file.read()))
    image = np.array(image)

    return emotions_detector(image)
