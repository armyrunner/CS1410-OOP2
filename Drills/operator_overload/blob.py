import math

KIND_PLAYER = 1
KIND_FOOD = 2
KIND_AI = 3

class Blob:

    def __init__(self, mass, x, y, world_width, world_height, kind):
        self.mMass = float(mass)  # mass
        self.mX = float(x)        # x position
        self.mY = float(y)        # y position
        self.mDx = 0.             # portion of speed that comes from x
        self.mDy = 0.             # portion of speed that comes from y
        self.mKind = kind         # kind of blob
        self.mAlive = True        # blob's life status

        # size of the world, used for bounding motion
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        # used to scale the speed to tune game play
        self.mSpeedMultiplier = 10.0
        # used to scale the display size of blobs
        self.mRadiusMultiplier = 5.0
        # used to make sure 1 frame's motion doesn't overshoot the destination
        self.mDestinationSpeed = 0.0
        return

    def getMass(self):
        return self.mMass

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getAlive(self):
        return self.mAlive

    def getKind(self):
        return self.mKind

    def getSpeed(self):
        mass = math.log(self.mMass)

        if float(self.mDestinationSpeed) < float(self.mSpeedMultiplier)/mass:
            self.mSpeed = self.mDestinationSpeed
        else:
            self.mSpeed = float(self.mSpeedMultiplier)/mass
        return self.mSpeed

    def getRadius(self):

        self.mRadius = self.mRadiusMultiplier * math.sqrt(self.mMass/math.pi)

        return self.mRadius

    def __ne__(self,other):

        if self.mX != other and self.mY != other:
            return True
        else:
            return False

    def __gt__(self,other):

        x = float(self.mMass / other.mMass)

        if x < 1.25:
            return False

        return True

    def __iadd__(self,other):

        self.mMass = self.mMass + other.mMass

        other.mMass = 0

        other.mAlive = False

        return self

    def __xor__(self,other):

        d = math.sqrt((other.mX - self.mX)**2 + (other.mY-self.mY)**2)

        if self.getRadius() > other.getRadius():
            if self.getRadius() > d:
                return True
        else:
            if other.getRadius() > d:
                return True

        return False

    def __ilshift__(self,position):

        newx = position[0] - self.mX
        newy = position[1]- self.mY

        d = math.sqrt((newx)**2 + (newy)**2))

        self.mDestinationSpeed = d

        if d > 0:
            self.mDx = newx/d
            self.mDy = newy/d

        else:
            self.mDy = 0
            self.mDx = 0

        return self

    def __irshift__(self, distance):

        self.mX = self.mX + (self.mDx * distance)
        self.mY = self.mY + (self.mDy * distance)


        if self.mX + self.getRadius() > self.mWorldWidth:
            self.mX = self.mWorldWidth - self.getRadius()

        elif self.mX + self.getRadius() < 0:
            self.mX = self.mWorldWidth + self.getRadius()

        if self.mY + self.getRadius() > self.mWorldHeight:
            self.mY = self.mWorldHeight - self.getRadius()

        elif self.mY + self.getRadius() < 0:
            self.mY = self.mWorldHeight + self.getRadius()

        return self
