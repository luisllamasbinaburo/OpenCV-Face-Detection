import cv2
import sys
import datetime as dt
from time import sleep

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

camera  = cv2.VideoCapture(0)

previous = 0
while True:
    if not camera .isOpened():
        print('Error al iniciar camara')
        sleep(5)
        pass

    ret, frame = camera .read()

    faces = faceCascade.detectMultiScale(
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Dibujar rectangulo en las caras
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    if previous != len(faces):
        previous = len(faces)
        print("Detected: "+str(len(faces))+ " " + str(dt.datetime.now()));
        sys.stdout.flush();

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera .release()
cv2.destroyAllWindows()
