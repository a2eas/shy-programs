import cv2
from detect_face import detect_faces
import os
from Closetabs import close_tabs



def on(video_frame):
        #using a function improted from detectface.py
        face_count,conf = detect_faces(video_frame)
        print('face_Count' , face_count)
        #showing the image with the face detected
        if face_count > 1:
            close_tabs()
        