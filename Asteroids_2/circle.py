import rotatable
import pygame

class Circle(rotatable.Rotatable):

    def __init__(self, x, y, dx, dy, rotation, radius, width, height):
        rotatable.Rotatable.__init__(self,x, y, dx, dy, rotation, width, height)
        self.mRadius = radius
        self.mColor = (255,255,255)

    
    def getRadius(self):
        return self.mRadius

    def getColor(self):
        return self.mColor

    def setColor(self,color):
        self.mColor = color

    def setRadius(self,radius):
        if radius >= 1:
            self.mRadius = radius

    def drawcircle(self,surface):
        pos = (int(self.mX),int(self.mY))
        pygame.draw.circle(surface,self.mColor, pos, self.mRadius, 0)

    def draw(self,surface):
        self.drawcircle(surface)
        
        