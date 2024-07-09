# ------------ Information ------------
# Author: Michievous Li
# Date：2024.7.9
# Usage：This file aims to list the available device.
# Reference：Orignal
# My_Github：https://github.com/mischievousx/Video_HDMI_Capture
# -------------------------------------

import cv2

for device_id in range(10):  
    cap = cv2.VideoCapture(device_id)
    if cap.isOpened():
        print(f"deviceID: {device_id} is available")
        cap.release()
    else:
        print(f"deviceID: {device_id} is unavailable")