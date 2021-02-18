#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

import cv2

class Webcam(object):

    def __init__(self):
        self.cv2 = cv2;
        self.cv2.namedWindow("preview");
        self.vc = self.cv2.VideoCapture(0);

        if self.vc.isOpened(): # try to get the first frame
            self.rval, self.frame = self.vc.read();
        else:
            self.rval = False;

        while self.rval:
            self.cv2.imshow("preview", self.frame);
            self.rval, self.frame = self.vc.read();
            self.key = self.cv2.waitKey(20);
            if self.key == 27: # exit on ESC
                break;
        self.cv2.destroyWindow("preview")

Webcam();
