import cv2
from video_cap import *
from object_screen import *
from detect_motion import *
import pygame

motion_detector = DetectMotion()
video = VideoCapture(motion_detector)
objectScreen = ObjectScreen(video.width,video.height,30)
clock = pygame.time.Clock()
fps = 120

while (video.imageCaptureOpened()):

    video.process()
    objectScreen.update(video.getCentroidTuple(),motion_detector.isZooming(),
    motion_detector.typeOfZoom(),motion_detector.getScalar(video.getCurrentArea()))

    k = cv2.waitKey(10)
    if k == 27:
        break

    clock.tick(fps)

