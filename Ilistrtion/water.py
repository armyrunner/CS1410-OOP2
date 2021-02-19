import pygame

class Water:

    def __init__(self,width,height):
        self.p1 = (int(width*.375),int(height*.85))
        self.p2 = (width,int(height*.85))
        self.p3 = (width,height)
        self.mPoints1 = [self.p1,self.p2,self.p3]
        self.mColor1 = (97,225,225)

        return

    def draw(self,surface):
        pygame.draw.polygon(surface,self.mColor1,self.mPoints1,0)
        return
