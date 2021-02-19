import pygame

class Moon:

    def __init__(self,width,height):
        self.mPos = (int(width*.9),int(height*.08))
        self.mRadius = 28
        self.mColor = (255,255,255)
        return

    def draw(self,surface):
        pygame.draw.circle(surface,self.mColor,self.mPos,self.mRadius,0)
        return
