import cv2
from video_cap import *

video = VideoCapture()

while (video.imageCaptureOpened()):
    
    video.readVideoImage()
    video.findMaxArea()
    video.findAndDrawCentroid()
    video.drawConvexPoints()

    k = cv2.waitKey(10)
    if k == 27:
        break

