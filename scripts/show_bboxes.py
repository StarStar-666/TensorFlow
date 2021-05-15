#! /usr/bin/env python
# coding=utf-8

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

ID = 0
label_txt = "F:/slide_dataSets/slide/Voc_2007_line/data/main.txt"
image_info = open(label_txt).readlines()[ID].split()

image_path = image_info[0]
image = cv2.imread(image_path)
for bbox in image_info[1:]:
    bbox = bbox.split(",")
    print(bbox[0])
    print(bbox[1])
    image = cv2.rectangle(image,(int(float(bbox[2])),
                                 int(float(bbox[3]))),
                                (int(float(bbox[0])),
                                 int(float(bbox[1]))), (255,0,0), 2)

plt.imshow(image)
plt.show()
