import cv2
class DetectMotion:

    #thresholds para melhor uso do algoritmo
    threshold = 5000
    threshold_optimal = 2000
    area_optimal = 30000

    def __init__(self):
        self.movement = None
        self.zooming = False
        self.type_of_zoom = None
        self.frame = 0
        self.last_position = None
    
    def checkVariation(self,image,centroid):
        cv2.putText(image,"Movimento -> {0}".format(self.movement),(30,200),2,1.,(255,255,255))
        if(self.frame %10 !=0):
            return

        if(self.last_position is not None):
            if(self.last_position[0] > centroid[0] and (abs(self.last_position[1] - centroid[1])<70)):
                self.movement = "Direita"
            if(self.last_position[0] < centroid[0] and (abs(self.last_position[1] - centroid[1])<70)):
                self.movement = "Esquerda"
            if(self.last_position[1] > centroid[1] and (abs(self.last_position[0] - centroid[0])<70)):
                self.movement = "Cima"
            if(self.last_position[1] < centroid[1] and (abs(self.last_position[0] - centroid[0])<70)):
                self.movement = "Baixo"

        self.last_position = centroid
    
    def isZooming(self):
        return self.zooming
    
    def typeOfZoom(self):
        return self.type_of_zoom
    
    def checkAreas(self,image,centroid_tuple,current_area,contour):
        cv2.circle(image,centroid_tuple,5,[0,0,255],2)
        #in area optima
        if(current_area <= DetectMotion.area_optimal+DetectMotion.threshold_optimal and \
        current_area >= DetectMotion.area_optimal-DetectMotion.threshold_optimal):
            self.zooming = False
            self.type_of_zoom = None
            cv2.drawContours(image,[contour],0,(0,255,0),2)
            cv2.putText(image,"Area Optima",(30,150),2,1.,(255,255,255))
            
        elif((current_area <= DetectMotion.area_optimal+DetectMotion.threshold and \
        current_area >= DetectMotion.area_optimal+DetectMotion.threshold_optimal) or \
        (current_area <= DetectMotion.area_optimal-DetectMotion.threshold_optimal and \
         current_area >= DetectMotion.area_optimal-DetectMotion.threshold)):
            self.zooming = False
            self.type_of_zoom = None
            cv2.drawContours(image,[contour],0,(255,0,0),2)
            cv2.putText(image,"Area Razoavel",(30,150),2,1.,(255,255,255))
        
        elif(current_area >= DetectMotion.area_optimal+DetectMotion.threshold or \
        current_area <= DetectMotion.area_optimal-DetectMotion.threshold):
            self.zooming = True
            if(current_area >= DetectMotion.area_optimal+DetectMotion.threshold):
                self.type_of_zoom = False
                cv2.drawContours(image,[contour],0,(0,0,255),2)
                cv2.putText(image,"Zooming In",(30,150),2,1.,(255,255,255))
            if(current_area <= DetectMotion.area_optimal-DetectMotion.threshold):
                self.type_of_zoom = True
                cv2.drawContours(image,[contour],0,(0,0,255),2)
                cv2.putText(image,"Zooming Out",(30,150),2,1.,(255,255,255))
    
    def getScalar(self,current_area):
        scalar = abs((DetectMotion.area_optimal + DetectMotion.threshold)*1.-current_area*1.)
        return float(scalar/10000)
    
    def setFrame(self,frame):
        self.frame = frame
