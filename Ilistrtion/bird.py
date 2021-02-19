import pygame


class Bird:

    def __init__(self,height,width):
        self.mRect1 = pygame.Rect(int(width*.5),int(height*.05),int(width*.2),int(height*.16))
        self.mRect2 = pygame.Rect(int(width*.70),int(height*.05),int(width*.2),int(height*.16))
        self.mColor = (0,0,0)
        return

    def draw(self,surface):
        pygame.draw.arc(surface,self.mColor,self.mRect1,0.0,3.14,1)
        pygame.draw.arc(surface,self.mColor,self.mRect2,0.0,3.14,1)
        return
