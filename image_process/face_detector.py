import numpy as np
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

image_path = sys.argv[1]
face_cascade_path = 'haarcascade_frontalface_default.xml'

# init detector and image
face_cascade = cv2.CascadeClassifier(face_cascade_path)

src = cv2.imread(image_path)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
image_h, image_w = src_gray.shape[:2]

# detection
faces = face_cascade.detectMultiScale(src_gray, 1.2, 3)
max_rect_label = 0
max_rect_size = 0
for i, face in enumerate(faces):
    if face[2]*face[3] > max_rect_size:
        max_rect_label = i

max_face = faces[max_rect_label]
face_x = int(max_face[0] + max_face[2]/2)
face_y = int(max_face[1] + max_face[3]/2)

print(face_x, face_y)



