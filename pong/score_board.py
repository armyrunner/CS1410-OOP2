import pygame
from text import *

class ScoreBoard:


    def __init__(self,x,y,width,height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mServeStatus = 1
        self.mRightScore = 0
        self.mLeftScore = 0
        self.mRightBoard = Text("Player 2: ",x+160,y)
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getLeftScore(self):
        return self.mLeftScore

    def getRightScore(self):
        return self.mRightScore

    def getServeStatus(self):
        return self.mServeStatus

    def isGameover(self):
        if self.getServeStatus() >= 3:
            return True
        return False


    def scoreLeft(self):
        if self.mLeftScore < 9 and self.mRightScore < 9:
            self.mLeftScore += 1
            if self.mLeftScore == 9:
                self.mServeStatus = 3


    def scoreRight(self):
        if self.mRightScore < 9 and self.mLeftScore < 9:
            self.mRightScore += 1
            if self.mRightScore == 9:
                self.mServeStatus = 4

    def swapServe(self):
        if self.getServeStatus() == 1:
            self.mServeStatus = 2

        elif self.getServeStatus() == 2:
            self.mServeStatus = 1

    def draw(self,surface,):
        leftscore = "Player 1: " + str(self.mLeftScore)
        LeftBoard = Text(leftscore, self.mX*.6,self.mY)
        LeftBoard.setColor((250,250,0))
        LeftBoard.draw(surface)

        rightscore = "Player 2: " + str(self.mRightScore)
        LeftBoard = Text(rightscore, self.mX+160,self.mY)
        LeftBoard.setColor((250,250,0))
        LeftBoard.draw(surface)
