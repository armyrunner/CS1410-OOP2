import pygame

class Ground:

    def __init__(self,width,height):
        self.p1 = (0,height)
        self.p2 = (0,int(height*.85))
        self.p3 = (int(width*.375),int(height*.85))
        self.p4 = (int(width*.375),height)
        self.p5 = (int(width*.375),height)
        self.p6 = (int(width*.375),int(height*.85))
        self.p7 = (width, height)
        self.mPoints1 = [self.p1,self.p2,self.p3,self.p4]
        self.mPoints2 = [self.p5,self.p6,self.p7]
        self.mColor1 = (56,102,0)
        self.mColor2 = (127,107,85)

        return

    def draw(self,surface):
        pygame.draw.polygon(surface,self.mColor1,self.mPoints1,0)
        pygame.draw.polygon(surface,self.mColor2,self.mPoints2,0)
        return
