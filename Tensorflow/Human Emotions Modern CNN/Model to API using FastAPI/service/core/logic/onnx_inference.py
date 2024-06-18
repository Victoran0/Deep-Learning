import onnx_runtime as rt
import cv2
import numpy as np


def emotions_detector(img_array):

    providers = ['CPUExecutionProvider']
    m_q = rt.InferenceSession(
        "eff_quantized.onnx", providers=providers)

    print(test_image.shape)
    test_image = cv2.resize(
        test_image, (256, 256))
    im = np.float32(test_image)
    img_array = np.expand_dims(im, axis=0)
    print(img_array.shape)

    onnx_pred = m_q.run(['dense'], {"input": img_array})
    print(np.argmaxnp.argmax(onnx_pred[0][0]))

    if np.argmaxnp.argmax(onnx_pred[0][0]) == 0:
        emotion = 'angry'
    elif np.argmaxnp.argmax(onnx_pred[0][0]) == 1:
        emotion = 'happy'
    else:
        emotion = 'sad'

    return {"emotion": emotion}
