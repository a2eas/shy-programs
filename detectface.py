import cv2
from mtcnn import MTCNN



def detect_faces(image):
    # Initialize the MTCNN face detector
    detector = MTCNN()

    # Detect faces in the image
    faces = detector.detect_faces(image)

    # Draw bounding boxes around the faces
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(faces)
    # Show the result
    return len(faces)


