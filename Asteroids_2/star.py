import circle
import random

class Star(circle.Circle):


    def __init__(self, x, y,width, height):
        rotation = 0
        radius = 2
        dx = 0 
        dy = 0
        circle.Circle.__init__(self,x, y, dx, dy, rotation, radius, width, height)
        self.mBrightness = (random.uniform(0,255))
        self.mSwitch = random.randint(1,3)

    def getBrightness(self):
        return self.mBrightness

    def setBrightness(self,brightness):
        if brightness >= 0 and brightness <= 255:
            self.mBrightness = brightness
            self.mColor = (brightness,brightness,brightness)

    def evolve(self, dt):
        self.mSwitch = random.randint(1,3)
        if self.mSwitch == 1:
            self.setBrightness(self.mBrightness + 10)
        elif self.mSwitch == 2:
            self.setBrightness(self.mBrightness - 10)
        else:
            self.setBrightness(self.mBrightness)          
    


