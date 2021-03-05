#!/usr/bin/python3
import cv2 as cv

# img = cv.imread('photos/kep001.jpg');

# cv.imshow('Kep', img);

# Reading videos
capture = cv.VideoCapture("videos/Youtube.mp4");

while True:
    isTrue, frame = capture.read();
    cv.imshow("Video", frame);

    if cv.waitKey(20) & 0xFF==ord('d'):
        break;

capture.release();
cv.destroyAllWindows();