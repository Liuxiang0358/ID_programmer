# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 20:47:55 2019

@author: lx
"""

from __future__ import division

from models import *
from utils.utils import *
from utils.datasets import *

import os
import time
import argparse
from PIL import Image
import torchvision.transforms as transforms
import torch
from torch.autograd import Variable

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator
conf_thres = 0.90
nms_thres = 0.3
img_size = 416
weights_path = "checkpoints/yolov3_ckpt_195.pth"
class_path = "utils/classes.names"
n_cpu = 0
model_def = "utils/yolov3-custom.cfg"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
os.makedirs("output", exist_ok=True)
classes = load_classes(class_path)  # Extracts class labels from file
    # Set up model
model = Darknet(model_def, img_size=img_size).to(device)

if weights_path.endswith(".weights"):
# Load darknet weights
    model.load_darknet_weights(weights_path)
else:
# Load checkpoint weights
    model.load_state_dict(torch.load(weights_path))

model.eval()  # Set in evaluation mode
def detect_second(file,img):
#    file = 'upload/0c8fe897-5f64-4913-a079-f9506c944c92id-face-img.jpg'
    time_Take = time.time()
    file = file
    img_origal = Image.fromarray(img)
#    img_origal = Image.open(file)
    img = transforms.ToTensor()(img_origal )
    img, _ = pad_to_square(img, 0)
    img = resize(img, img_size)
    img = img.reshape((1,img.shape[0],img.shape[1],img.shape[2]))
    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    img_detections = []  # Stores detections for each image index
    input_imgs = Variable(img.type(Tensor))

    # Get detections
    with torch.no_grad():
        detections = model(input_imgs )
        detections = non_max_suppression(detections, conf_thres,nms_thres)
    img_detections.extend(detections)

    for img_i, ( detections) in enumerate(zip( img_detections)):


        # Create plot
        img_array = np.array(img_origal)

        # Draw bounding boxes and labels of detections
        local = []
        if detections is not None:
            # Rescale boxes to original image
#            print(detections)
            detections = rescale_boxes(detections[0], img_size, img_array.shape[:2])
            unique_labels = detections[:, -1].cpu().unique()
            for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections:
                local.append([str(int(cls_pred)),str(float(x1)),str(float(y1)), str(float(x2)),str(float(y2))])

        filename = file.split(".")[0]
#        plt.savefig(f"output/{filename}.png", bbox_inches="tight", pad_inches=0.0)
        with open(f"{filename}.txt","w") as f:
          for l in local:
              f.writelines(str(l)+'\n')
    print(time.time() - time_Take)