class Movable:


    def __init__(self,x,y,dx,dy,width,height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = width
        self.mWorldHeight = height


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


    def accelerate(self,delta_velocity):
         raise NotImplementedError

    def evolve(self,dt):
        raise NotImplementedError

    def draw(self,surface):
        raise NotImplementedError
