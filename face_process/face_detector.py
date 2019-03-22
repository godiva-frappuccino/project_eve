import numpy as np
import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

image_path = sys.argv[1]

class FaceDetector:
    def __init__(self):
        face_cascade_path = 'models/haarcascade_frontalface_default.xml'
        # init detector and image
        self.classifier = cv2.CascadeClassifier(face_cascade_path)

    def detect(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_h, image_w = image.shape[:2]

        # detection
        faces = self.classifier.detectMultiScale(image, 1.2, 3)
        max_rect_label = 0
        max_rect_size = 0
        for i, face in enumerate(faces):
            if face[2]*face[3] > max_rect_size:
                max_rect_label = i

        max_face = faces[max_rect_label]
        face_x = int(max_face[0] + max_face[2]/2)
        face_y = int(max_face[1] + max_face[3]/2)

        return face_x, face_y




