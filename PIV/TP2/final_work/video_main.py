import cv2
from video_cap import *
from object_screen import *
from detect_motion import *
import pygame

class VideoMain:
    
    clock = pygame.time.Clock()
    fps = 120

    def __init__(self):
        self.main = None
        self.motion_detector = DetectMotion()
        self.video = VideoCapture(self.motion_detector)
        self.objectScreen = ObjectScreen(self.video.width,self.video.height,30)
    
    def video_loop(self):
        while (self.video.imageCaptureOpened()):

            self.video.process()
            self.objectScreen.update(self.video.getCentroidTuple(),self.motion_detector.isZooming(),
            self.motion_detector.typeOfZoom(),self.motion_detector.getScalar(self.video.getCurrentArea()))

            k = cv2.waitKey(10)
            if k == 27:
                break

            VideoMain.clock.tick(VideoMain.fps)

if __name__ == "__main__":
    video_main = VideoMain()
    video_main.video_loop()
