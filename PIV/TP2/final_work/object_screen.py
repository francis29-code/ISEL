from pygame import * 
import sys


class ObjectScreen:

    backgroundColor = (255,200,50)
    base_zoom_factor = 20

    def __init__(self,width,height,squareSize):
        self.width = width
        self.height = height
        self.screen = display.set_mode((self.width,self.height))
        self.screen.fill(ObjectScreen.backgroundColor)
        self.squareSize = squareSize
        self.top_corner = None
        self.bottom_corner = None

    def rectangleDraw(self,centroid):
        self.top_corner = (centroid[0]-self.squareSize,centroid[1]-self.squareSize)
        self.bottom_corner = (self.squareSize*2,self.squareSize*2)
        draw.rect(self.screen,(0,0,0),(self.top_corner,self.bottom_corner),0)
        # raise NotImplementedError
    
    def zoomSquare(self,centroid,type_zoom,scalar):
        #when type is false, zooms in, otherwise zoomsout
        #scalar is an integer that defines how much it scales
        self.top_corner = (centroid[0]-self.squareSize,centroid[1]-self.squareSize)
        self.bottom_corner = (self.squareSize*2,self.squareSize*2)

        x_top = self.top_corner[0] 
        y_top = self.top_corner[1] 
        x_bottom = self.bottom_corner[0]
        y_bottom = self.bottom_corner[1]

        if(type_zoom):
            #zoomout
            self.top_corner = (x_top + ObjectScreen.base_zoom_factor*scalar,y_top + ObjectScreen.base_zoom_factor*scalar)
            self.bottom_corner = (x_bottom - 2*(ObjectScreen.base_zoom_factor*scalar),y_bottom - 2*(ObjectScreen.base_zoom_factor*scalar))
            draw.rect(self.screen,(0,0,0),(self.top_corner,self.bottom_corner),0)
        else:
            #zoom in
            self.top_corner = (x_top-ObjectScreen.base_zoom_factor*scalar,y_top-ObjectScreen.base_zoom_factor*scalar)
            self.bottom_corner = (x_bottom+2*(ObjectScreen.base_zoom_factor*scalar),y_bottom+2*(ObjectScreen.base_zoom_factor*scalar))
            draw.rect(self.screen,(0,0,0),(self.top_corner,self.bottom_corner),0)


    def update(self,position,zooming,type_of_zoom,scalar):
        self.screen.fill(ObjectScreen.backgroundColor)
        if(not zooming):
            self.rectangleDraw(position)
        else:
            self.zoomSquare(position,type_of_zoom,scalar)
        self.checkEvents()
        display.update()

    def checkEvents(self):
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()




