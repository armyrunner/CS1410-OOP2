import pygame
import random

class Ball:

    def __init__(self,mSize,mMinX,mMaxX,mMinY,mMaxY,mLeftPaddleX,mRightPaddleX):
        self.mX = mMinX
        self.mY = mMinY
        self.mDX = 0
        self.mDY = 0
        self.mSize = mSize
        self.mMinX = mMinX
        self.mMaxX = mMaxX
        self.mMinY = mMinY
        self.mMaxY = mMaxY
        self.mLeftPaddleX = mLeftPaddleX
        self.mLeftPaddleMinY = mMinY
        self.mLeftPaddleMaxY = mMaxY
        self.mRightPaddleX = mRightPaddleX
        self.mRightPaddleMinY = mMinY
        self.mRightPaddleMaxY = mMaxY

        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getSize(self):
        return self.mSize

    def getMinX(self):
        return self.mMinX

    def getMaxX(self):
        return self.mMaxX

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getLeftPaddleX(self):
        return self.mLeftPaddleX

    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY

    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY

    def getRightPaddleX(self):
        return self.mRightPaddleX

    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY

    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY

    def setPosition(self,x,y):
        if x > self.mMinX and x < (self.mMaxX - self.mSize):
            if y > self.mMinY and y < (self.mMaxY - self.mSize):
                self.mX = x
                self.mY = y
                return True
        else:
            return False

    def setSpeed(self, dx, dy):
        self.mDX = dx
        self.mDY = dy


    def setLeftPaddleY(self,paddle_min_y,paddle_max_y):
        if self.mMinY <= paddle_min_y:
            if paddle_min_y <= paddle_max_y:
                if paddle_max_y <= self.mMaxY:
                    self.mLeftPaddleMinY = paddle_min_y
                    self.mLeftPaddleMaxY = paddle_max_y
        #             return True
        # else:
        #     return False

    def setRightPaddleY(self,paddle_min_y,paddle_max_y):
        if self.mMinY <= paddle_min_y:
            if paddle_min_y <= paddle_max_y:
                if paddle_max_y <= self.mMaxY:
                    self.mRightPaddleMinY = paddle_min_y
                    self.mRightPaddleMaxY = paddle_max_y
        #             return True
        # else:
        #     return False

    def checkTop(self,new_y):
        if new_y > self.mMinY:
            return new_y
        else:
            new_y = 2*self.mMinY - new_y
            self.mDY = -self.mDY
            return new_y
            
    def checkBottom(self,new_y):
        if (new_y + self.mSize) <= self.mMaxY:
            return new_y
        else:
            dy = (new_y + self.mSize) - self.mMaxY
            new_y = self.mMaxY - dy - self.mSize
            self.mDY = -self.mDY
            return new_y

    def checkLeft(self,new_x):
        if new_x > self.mMinX:
            return new_x
        else:
            new_x = self.mMinX
            self.mDX = 0
            self.mDY = 0
            return new_x

    def checkRight(self,new_x):

        if (new_x + self.mSize) < self.mMaxX:
            return new_x
        else:
            new_x = self.mMaxX - self.mSize
            self.mDX = 0
            self.mDY = 0
            return new_x

    def checkLeftPaddle(self,new_x,new_y):
        if self.mDX < 0:
            if self.mX > self.mLeftPaddleX:
                if new_x <= self.mLeftPaddleX:
                    mid_y = self.mY + (new_y-self.mY)/2
                    if mid_y >= self.mLeftPaddleMinY:
                        if mid_y <= self.mLeftPaddleMaxY:
                            dx = self.mLeftPaddleX - new_x
                            new_x = self.mLeftPaddleX + dx
                            self.mDX = -self.mDX
                            return new_x
        return new_x

    def checkRightPaddle(self,new_x,new_y):
        if self.mDX > 0:
            if (self.mX+self.mSize) < self.mRightPaddleX:
                if (new_x + self.mSize) >= self.mRightPaddleX:
                    mid_y = self.mY + (new_y - self.mY)/2
                    if mid_y >= self.mRightPaddleMinY:
                        if mid_y <= self.mRightPaddleMaxY:
                            dx = (new_x + self.mSize) - self.mRightPaddleX
                            new_x = self.mRightPaddleX -(dx + self.mSize)
                            self.mDX = -self.mDX
                            return new_x

        return new_x

    def move(self,dt):
        new_x = self.mX + self.mDX * dt
        new_y = self.mY + self.mDY * dt
        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)
        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)
        new_x = self.checkLeftPaddle(new_x,new_y)
        new_x = self.checkRightPaddle(new_x,new_y)
        self.mX = new_x
        self.mY = new_y
        return

    def serveLeft(self,x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = random.uniform(min_y, max_y)
        self.mDX = random.uniform(min_dx, max_dx)
        self.mDY = random.uniform(min_dy, max_dy)
        return


    def serveRight(self,x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = random.uniform(min_y, max_y)
        self.mDX = random.uniform(-min_dx, -max_dx)
        self.mDY = random.uniform(min_dy, max_dy)
        return

    def draw(self,surface):
        color = (250,250,250)
        width = self.mSize
        height = self.mSize
        rect = pygame.Rect(self.mX,self.mY,width,height)
        pygame.draw.rect(surface,color,rect,0)
