import math

class Movable:


    def __init__(self,x,y,dx,dy,width,height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = width
        self.mWorldHeight = height
        self.mActive = True


    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getActive(self):
        return self.mActive

    def move(self,dt):
        self.mX += self.mDX*dt
        self.mY += self.mDY*dt

        if self.mX <= 0:
            self.mX += self.mWorldWidth

        if self.mX >= self.mWorldWidth:
            self.mX -= self.mWorldWidth

        if self.mY <= 0:
            self.mY += self.mWorldHeight

        if self.mY >= self.mWorldHeight:
            self.mY -= self.mWorldHeight
    
    def setActive(self,active):
        self.mActive = active

    def hits(self,other):

        d = math.sqrt((other.mX - self.mX)**2 + (other.mY- self.mY)**2)
        radius_added = self.getRadius() + other.getRadius()

        if d <= radius_added:
            return True
        else:
            return False
  
    def getRadius(self):
        raise NotImplementedError

    def accelerate(self,delta_velocity):
         raise NotImplementedError

    def evolve(self,dt):
        raise NotImplementedError

    def draw(self,surface):
        raise NotImplementedError
