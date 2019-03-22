import cv2
import numpy as np
from get_image import CameraModule
from face_detector import FaceDetector
import time
from motor import Motor

def main():
    # init
    camera = CameraModule()
    detector = FaceDetector()
    motor = Motor()
    while True:
        # detect human        
        image = camera.get_image()
        position_diff = detector.get_position()
        # sleep
        time.sleep(0.5)
        # face move
        motor.adjust(position_diff)
        # sleep
        time.sleep(0.5)
