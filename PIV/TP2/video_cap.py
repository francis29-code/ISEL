import cv2

class VideoCapture:

    max_area = 0

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.cx = 0
        self.cy = 0
        self.image = None
        self.binarized = None
        self.contour = None

    def imageCaptureOpened(self):
        return self.video.isOpened()

    def readVideoImage(self):
        ret, self.image = self.video.read()
        gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        ret, self.binarized = cv2.threshold(blur,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow("binarizada",self.binarized)

    def findMaxArea(self):
        nonsense, contours, hierarchy = cv2.findContours(self.binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contourToDraw = 0
        VideoCapture.max_area = 0
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            if(area > VideoCapture.max_area):
                VideoCapture.max_area = area
                contourToDraw = i
        self.contour = contours[contourToDraw]
    
    def findAndDrawCentroid(self):
        hull = cv2.convexHull(self.contour)
        moments = cv2.moments(self.contour)
        if moments['m00']!=0:
            self.cx = int(moments['m10']/moments['m00']) # cx = M10/M00
            self.cy = int(moments['m01']/moments['m00']) # cy = M01/M00
        centr=(self.cx,self.cy)
        cv2.circle(self.image,centr,5,[0,0,255],2)
        cv2.drawContours(self.image,[self.contour],0,(0,255,0),2)
        # cv2.drawContours(self.image,[hull],0,(255,0,0),2)
        cv2.imshow("input",self.image)

    def drawConvexPoints(self):
        hull = cv2.convexHull(self.contour)
        for point in hull:
            p = (int(point[0][0]),int(point[0][1]))
            cv2.circle(self.image,p,5,[0,0,255],2)
 
    
    def getCentroidTuple(self):
        return tuple(self.cx,self.cy)

    def getCentroidX(self):
        return self.cx
    
    def getCentroidY(self):
        return self.cy

    def getCurrentArea(self):
        return cv2.contourArea(self.contour)
    
   
            


