import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import argparse
import os

def fromImage(image, face_cascade, scaleFactor=1.5, minNeighbors=6):
	image_copy = image.copy()
	gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

	face_cascade = cv2.CascadeClassifier(face_cascade)
	eye_cascade = cv2.CascadeClassifier(eye_cascade)

	faces_rects = face_cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors);

	print('Found', len(faces_rects), 'face')

	for (x,y,w,h) in faces_rects:
		 cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 0, 255), 2)

	plt.imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))
	plt.show()

def fromWebCam(face_cascade, eye_cascade):
	video_capture = cv2.VideoCapture(0)
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
	while True:
		ret, frame = video_capture.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		faces = face_cascade.detectMultiScale(
			gray,
			scaleFactor=1.5,
			minNeighbors=5,
			minSize=(40, 40),
			flags=cv2.CASCADE_SCALE_IMAGE)

		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]

			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

		cv2.imshow('FaceDetection', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	video_capture.release()
	cv2.destroyAllWindows()	

if __name__ == "__main__":
	face_cascade = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
	eye_cascade = cv2.data.haarcascades + "haarcascade_eye.xml"
	image = cv2.imread('images/test_image.jpeg')
	#fromImage(image, face_cascade)
	fromWebCam(face_cascade, eye_cascade)