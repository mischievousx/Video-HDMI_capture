# ------------ Information ------------
# Author: Michievous Li
# Date：2024.7.9
# Usage：This file aims to display the video data in python and process the video data
# Reference：Orignal
# My_Github：
# -------------------------------------

import cv2

for device_id in range(10):  
    cap = cv2.VideoCapture(device_id)
    if cap.isOpened():
        print(f"deviceID: {device_id} is available")
        cap.release()
    else:
        print(f"deviceID: {device_id} is unavailable")