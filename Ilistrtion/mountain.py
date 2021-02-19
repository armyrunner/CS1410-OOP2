import pygame

class Mountain:

    def __init__(self,width,height):
        self.p1 = (0,height)
        self.p2 = (0,int(height*.75))
        self.p3 = (int(width*.25),int(height*.333))
        self.p4 = (int(width*.5),int(height*.667))
        self.p5 = (int(width*.75),int(height*.5))
        self.p6 = (width,int(height*.875))
        self.p7 = (width, height)
        self.mPoints1 = [self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7]
        self.mColor1 = (173,146,116)

        return

    def draw(self,surface):
        pygame.draw.polygon(surface,self.mColor1,self.mPoints1,0)
        return
