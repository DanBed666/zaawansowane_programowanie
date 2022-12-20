import base64

import cv2 as cv
from PIL import Image
from io import BytesIO


def pict(name):
    countx = []

    cvNet = cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')

    img = cv.imread(name)
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet.forward()

    for detection in cvOut[0, 0, :, :]:
        score = float(detection[2])
        # ustawienie odpowiedniej wagi
        if score > 0.6:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            countx.append(score)
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 100, 75), thickness=4)
            print(score)

    print(type(img))
    im = Image.fromarray(img)
    im.thumbnail((800, 800), Image.ANTIALIAS)
    buffered = BytesIO()
    im.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    print(type(im))
    print(type(img_str))

    return len(countx), img_str
