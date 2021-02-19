import rotatable
import pygame
import math


class Polygon(rotatable.Rotatable):

    def __init__(self,x,y,dx,dy,rotation,width,height):
        rotatable.Rotatable.__init__(self,x,y,dx,dy,rotation,width,height)
        self.mColor = (255,255,255)
        self.mOriginalPolygon = []


    def getPolygon(self):
        return self.mOriginalPolygon

    def getColor(self):
        return self.mColor

    def setPolygon(self,point_list):
        self.mOriginalPolygon = point_list

    def getRadius(self):
        
        if self.mOriginalPolygon == []:
            return 0

        total = 0

        for (x,y) in self.mOriginalPolygon:
            d = math.sqrt(x**2+y**2)
            total += d
        average = total/len(self.mOriginalPolygon)
        return average


    def setColor(self,color):
        goodcolor = True

        for color_channel in color:
            if color_channel < 0 or color_channel > 255:
                goodcolor = False
        if goodcolor:
            self.mColor = color

    def draw(self,surface):
        polypoints = self.getPolygon()
        point_list = self.rotateAndTranslatePointList(polypoints)
        pygame.draw.polygon(surface,self.mColor,point_list,2)
