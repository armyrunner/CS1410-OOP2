import pygame

class MyFrog:

    def __init__(self,width,height):
        self.mWidth = width
        self.mHeight = height
        #nose
        self.mRect1 = pygame.Rect(int(self.mWidth*.507),int(self.mHeight*.89),int(self.mWidth*.0291),int(self.mHeight*.05))
        #body
        self.mRect2 = pygame.Rect(int(self.mWidth*.5),int(self.mHeight*.9),int(self.mWidth*.043),int(self.mHeight*.05))
        #eyes
        self.mRect3 = pygame.Rect(int(self.mWidth*.5),int(self.mHeight*.9),int(self.mWidth*.008),int(self.mHeight*.01))
        self.mRect4 = pygame.Rect(int(self.mWidth*.535),int(self.mHeight*.9),int(self.mWidth*.008),int(self.mHeight*.01))
        #left leg
        self.mRect5 = pygame.Rect(int(self.mWidth*.495),int(self.mHeight*.939),int(self.mWidth*.008),int(self.mHeight*.02))
        self.mRect6 = pygame.Rect(int(self.mWidth*.488),int(self.mHeight*.95),int(self.mWidth*.008),int(self.mHeight*.03))
        self.mRect7 = pygame.Rect(int(self.mWidth*.483),int(self.mHeight*.965),int(self.mWidth*.008),int(self.mHeight*.01))
        #Right Leg
        self.mRect8 = pygame.Rect(int(self.mWidth*.539),int(self.mHeight*.939),int(self.mWidth*.008),int(self.mHeight*.02))
        self.mRect9 = pygame.Rect(int(self.mWidth*.545),int(self.mHeight*.95),int(self.mWidth*.008),int(self.mHeight*.03))
        self.mRect10 = pygame.Rect(int(self.mWidth*.55),int(self.mHeight*.965),int(self.mWidth*.008),int(self.mHeight*.01))
        #Left Arm
        self.mRect11 = pygame.Rect(int(self.mWidth*.495),int(self.mHeight*.92),int(self.mWidth*.008),int(self.mHeight*.01))
        self.mRect12 = pygame.Rect(int(self.mWidth*.488),int(self.mHeight*.89),int(self.mWidth*.008),int(self.mHeight*.03))
        self.mRect13 = pygame.Rect(int(self.mWidth*.483),int(self.mHeight*.895),int(self.mWidth*.008),int(self.mHeight*.01))
        #Right Arm
        self.mRect14 = pygame.Rect(int(self.mWidth*.54),int(self.mHeight*.92),int(self.mWidth*.008),int(self.mHeight*.01))
        self.mRect15 = pygame.Rect(int(self.mWidth*.547),int(self.mHeight*.89),int(self.mWidth*.008),int(self.mHeight*.03))
        self.mRect16 = pygame.Rect(int(self.mWidth*.552),int(self.mHeight*.895),int(self.mWidth*.008),int(self.mHeight*.01))
        #Color
        self.mColor1 = (204,0,0)
        self.mColor2 = (0,128,0)
        self.mColor3 = (204,0,0)
        return

    def draw(self,surface):
        #nose
        pygame.draw.rect(surface,self.mColor2,self.mRect1,0)
        #body
        pygame.draw.rect(surface,self.mColor2,self.mRect2,0)
        #eyes
        pygame.draw.rect(surface,self.mColor3,self.mRect3,0)
        pygame.draw.rect(surface,self.mColor3,self.mRect4,0)
        #Left Leg
        pygame.draw.rect(surface,self.mColor2,self.mRect5,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect6,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect7,0)
        #Right Leg
        pygame.draw.rect(surface,self.mColor2,self.mRect8,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect9,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect10,0)
        #LEft Arm
        pygame.draw.rect(surface,self.mColor2,self.mRect11,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect12,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect13,0)
        #Right Arm
        pygame.draw.rect(surface,self.mColor2,self.mRect14,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect15,0)
        pygame.draw.rect(surface,self.mColor2,self.mRect16,0)


        return
