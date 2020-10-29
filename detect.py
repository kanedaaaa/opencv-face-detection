import cv2
import numpy as np 
import matplotlib.pyplot as plt 

def detectFaces(image, scaleFactor=1.2, minNeighbors=6):
	image_copy = image.copy()
	gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

	cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

	faces_rects = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors);

	print('Found', len(faces_rects), 'face')

	for (x,y,w,h) in faces_rects:
	     cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 0, 255), 2)

	return image_copy

image = cv2.imread('images/test_image.jpeg')
detected_faces = detectFaces(image)

plt.imshow(cv2.cvtColor(detected_faces, cv2.COLOR_BGR2RGB))
plt.show()