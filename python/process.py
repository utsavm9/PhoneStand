url = "http://172.20.10.3/capture"

############################################
import urllib
import cv2
import requests
import numpy as np

from facenet_pytorch import MTCNN       # The Model

import torch                            # For finding if we have CUDA
import numpy                            # For shape of images
from torchvision import transforms      # To convert Tensors to PIL Images
from PIL import Image, ImageDraw        # Image processing

import serial
############################################



res = requests.get(url, stream=True)

######### Load the model
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print("Using", device)
mtcnn = MTCNN(select_largest=False, device=device)

ser = serial.Serial('/dev/cu.usbmodem2401')
print(ser.name)

while True:

    ######### Capturing an image frame
    #print("Capturing a frame")
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)


    ######### Covert to PIL
    image = Image.fromarray(img)
    image.thumbnail((500, 500), Image.ANTIALIAS)
    #print("Image size:", image.size)

    # Remove the alpha channel from a PNG because that is 
    # what MTCNN wants
    image = image.convert("RGB")

    #print("Image shape:", numpy.array(image).shape)


    ########### Inference
    box, prob, points = mtcnn.detect(image, landmarks=True)
    #print("Box:", box)

    boxedImage = image.copy()
    draw = ImageDraw.Draw(boxedImage)

    # Draw rectangle
    try:
        draw.rectangle(box[0], width=2)

        # Draw points
        for p in points[0]:
            #print("Point:", p)
            draw.rectangle([p[0] - 2, p[1] - 2, p[0] + 2, p[1] + 2], width=1)


        # Draw the center point of image
        centerW = image.size[0] / 2
        centerH = image.size[1] / 2
        r = 5
        draw.ellipse((centerW - r, centerH - r, centerW + r, centerH + r), fill=(0, 0, 255))

        # Draw the center point of the box
        faceW = box[0][0] + ((box[0][2] - box[0][0]) / 2)
        faceH = box[0][1] + ((box[0][3] - box[0][1]) / 2)
        r = 5
        draw.ellipse((faceW - r, faceH - r, faceW + r, faceH + r), fill=(0, 255, 255))
    except:
        pass


    open_cv_image = numpy.array(boxedImage)
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    cv2.imshow('test',open_cv_image)

    ########## Bounding box
    centerW = image.size[0] / 2
    centerH = image.size[1] / 2
    try:
        faceW = box[0][0] + ((box[0][2] - box[0][0]) / 2)
        faceH = box[0][1] + ((box[0][3] - box[0][1]) / 2)
    except:
        faceW = centerW
        faceH = centerH

    ########## Direction
    direction = (faceW - centerW) / (centerW)
    #print(direction)
    ######### Direction to send
    send = b"N"
    if direction < -0.2:
        send = b"L"
    if direction > 0.2:
        send = b"R" 

    d = "LEFT" if (direction < 0) else "RIGHT"
    print(send, "-", d, "by", "{0:.1%}".format(abs(direction)))
    ser.write(send)

    # all the opencv processing is done here
    if ord('q')==cv2.waitKey(10):
        exit(0)