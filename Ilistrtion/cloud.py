import pygame

class Cloud:

    def __init__(self,width,height):
        self.mRect = pygame.Rect(int(width*.05),int(height*.05),int(width*.4),int(height*.16))
        self.mColor = (169,169,169)

        return

    def draw(self,surface):
        pygame.draw.ellipse(surface,self.mColor,self.mRect,0)
        return
