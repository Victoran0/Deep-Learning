import onnxruntime as rt
import cv2
import numpy as np
import time
import service.main as s


def emotions_detector(img_array):

    # Check if image is in graysccale and convert to rgb
    if len(img_array.shape) == 2:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)

    time_init = time.time()

    # resize layer
    test_image = cv2.resize(img_array, (256, 256))
    im = np.float32(test_image)
    img_array = np.expand_dims(im, axis=0)

    time_elapsed_preprocessing = time.time() - time_init

    onnx_pred = s.m_q.run(['dense_2'], {"input_1": img_array})

    time_elapsed = time.time() - time_init

    if np.argmax(onnx_pred[0][0]) == 0:
        emotion = 'angry'
    elif np.argmax(onnx_pred[0][0]) == 1:
        emotion = 'happy'
    else:
        emotion = 'sad'

    return {
        "emotion": emotion,
        "time_elapsed": str(time_elapsed),
        "time_elapsed_preprocessing": str(time_elapsed_preprocessing)
    }
