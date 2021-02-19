import circle

class Bullet(circle.Circle):

    def __init__(self, x, y, dx, dy, rotation, width, height):
        radius = 3
        circle.Circle.__init__(self,x, y, dx, dy, rotation, radius, width, height)
        dv = 100
        dt = .1
        self.mAge = 0
        self.accelerate(dv)
        self.move(dt)
     

    def getAge(self):
        return self.mAge
    
    def setAge(self,age):
        self.mAge = age
    
    def evolve(self, dt):
        self.move(dt)
        self.mAge += dt
        if self.mAge >= 6:
            self.mActive = False
