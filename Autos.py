import cv2
from Rastreador import *

seguimiento = Rastreador()

cap = cv2.VideoCapture("avenida.mp4")


deteccion = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=12)

while True:
	ret, frame = cap.read()
	frame = cv2.resize(frame, (1280,720))
	zona = frame [530:720, 300:850]

	mascara = deteccion.apply(zona)
