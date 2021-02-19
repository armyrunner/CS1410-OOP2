import pygame


class Paddle:

    def __init__(self,x,y,width,height,speed,min_y,max_y):
        self.mX = x #top left corner of paddle
        self.mY = y #top left corner of paddle
        self.mWidth = width # vertical size of the paddle
        self.mHeight = height # hortizontal size of the paddle
        self.mSpeed = speed # vertical speed of the ball
        self.mMinY = min_y # top of wall
        self.mMaxY = max_y # bottom of wall

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getRightX(self):
        xright = self.mWidth + self.mX
        return xright

    def getBottomY(self):
        ybottom = self.mHeight + self.mY
        return ybottom

    def getPositon(self):
        return self.mY

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getSpeed(self):
        return self.mSpeed

    def setPosition(self,new_y):
        if new_y < self.mMinY:
           self.mY= self.mMinY
        elif (new_y + self.mHeight) > self.mMaxY:
            self.mY = self.mMaxY-self.mHeight
        else:
            self.mY = new_y

    def moveUp(self,dt):
        new_y = self.mY - (self.mSpeed * dt)
        if new_y < self.mMinY:
            self.mY = self.mMinY
        else:
            self.mY = new_y


    def moveDown(self,dt):
        new_y = self.mY + (self.mSpeed * dt)
        if (new_y + self.mHeight) > self.mMaxY:
            self.mY = self.mMaxY - self.mHeight
        else:
            self.mY = new_y

    def draw(self,surface):
        color = (250,250,250)
        rect = pygame.Rect(self.mX,self.mY,self.mWidth,self.mHeight)
        pygame.draw.rect(surface,color,rect,0)
