import pygame

class House:

    def __init__(self,width,height):
        self.p1 = (int(width*.2),int(height*.3))
        self.p2 = (int(width*.3),int(height*.5))
        self.p3 = (int(width*.02),int(height*.5))
        self.mPoints1 = [self.p1,self.p2,self.p3]
        self.mRect1 = pygame.Rect(int(width*.05),int(height*.5),int(width*.235),int(height*.35))
        self.mRect2 = pygame.Rect(int(width*.18),int(height*.74),int(width*.05),int(height*.11))
        self.mPos = (int(width*.22),int(height*.8))
        self.mRadius = 3
        self.mColor1 = (229, 217, 189 )
        self.mColor2 = (255,0,0)
        self.mColor3 = (183, 65, 14)
        self.mColor4 = (255,255,255)

        return

    def draw(self,surface):
        pygame.draw.rect(surface,self.mColor1,self.mRect1,0)
        pygame.draw.rect(surface,self.mColor3,self.mRect2,0)
        pygame.draw.polygon(surface,self.mColor2,self.mPoints1,0)
        pygame.draw.circle(surface,self.mColor4,self.mPos,self.mRadius,0)
        return
