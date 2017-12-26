import cv2
class DetectMotion:

    #thresholds para melhor uso do algoritmo
    threshold = 5000
    threshold_optimo = 2000
    area_optima = 30000

    def __init__(self):
        self.movimento = None
        self.zooming = False
        self.type_of_zoom = None
    
    def checkVariation(self):
        raise NotImplementedError
    
    def isZooming(self):
        return self.zooming
    
    def typeOfZoom(self):
        return self.type_of_zoom
    
    def checkAreas(self,image,centroid_tuple,current_area,contour):
        cv2.circle(image,centroid_tuple,5,[0,0,255],2)
        #in area optima
        if(current_area <= DetectMotion.area_optima+DetectMotion.threshold_optimo and \
        current_area >= DetectMotion.area_optima-DetectMotion.threshold_optimo):
            self.zooming = False
            self.type_of_zoom = None
            cv2.drawContours(image,[contour],0,(0,255,0),2)
            cv2.putText(image,"Area Optima",(30,150),2,1.,(255,255,255))
            
        elif((current_area <= DetectMotion.area_optima+DetectMotion.threshold and \
        current_area >= DetectMotion.area_optima+DetectMotion.threshold_optimo) or \
        (current_area <= DetectMotion.area_optima-DetectMotion.threshold_optimo and \
         current_area >= DetectMotion.area_optima-DetectMotion.threshold)):
            self.zooming = False
            self.type_of_zoom = None
            cv2.drawContours(image,[contour],0,(255,0,0),2)
            cv2.putText(image,"Area Razoavel",(30,150),2,1.,(255,255,255))
        
        elif(current_area >= DetectMotion.area_optima+DetectMotion.threshold or \
        current_area <= DetectMotion.area_optima-DetectMotion.threshold):
            self.zooming = True
            if(current_area >= DetectMotion.area_optima+DetectMotion.threshold):
                self.type_of_zoom = False
                cv2.drawContours(image,[contour],0,(0,0,255),2)
                cv2.putText(image,"Zooming In",(30,150),2,1.,(255,255,255))
            if(current_area <= DetectMotion.area_optima-DetectMotion.threshold):
                self.type_of_zoom = True
                cv2.drawContours(image,[contour],0,(0,0,255),2)
                cv2.putText(image,"Zooming Out",(30,150),2,1.,(255,255,255))
    
    def getScalar(self,current_area):
        scalar = abs((DetectMotion.area_optima + DetectMotion.threshold)*1.-current_area*1.)
        return float(scalar/10000)
