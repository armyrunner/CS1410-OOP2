import pygame

class Sky:

    def __init__(self,width,height):
        self.mRect = pygame.Rect(0,0,width,height)
        self.mColor = (17,9,140)
        return

    def draw(self,surface):
        pygame.draw.rect(surface,self.mColor,self.mRect,0)
        return
