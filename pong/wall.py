import pygame


class Wall:


    def __init__(self,x,y,width,height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getRightX(self):
        return self.mWidth + self.mX


    def getBottomY(self):
        return self.mHeight + self.mY


    def draw(self,surface):
        Color = (250,250,250)
        Rect = pygame.Rect(self.mX,self.mY,self.mWidth,self.mHeight)
        pygame.draw.rect(surface,Color,Rect,0)
