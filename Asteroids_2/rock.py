import polygon
import random
import math


class Rock(polygon.Polygon):

    def __init__(self,x,y,width,height):
        dx = 0
        dy = 0
        rotation = random.uniform(0.0,359.9)
        polygon.Polygon.__init__(self,x,y,dx,dy,rotation,width,height)
        self.mSpinRate = random.uniform(-90,90)
        self.accelerate(random.randint(10,20))
        radius = random.uniform(10,30)
        num_points = random.randint(6,12)
        self.setPolygon(self.createRandomPolygon(radius,num_points))


    def createRandomPolygon(self,radius,points):
        point_list = []
        theta = 360/points
        for i in range(points):
            r = random.uniform(radius*.7,radius*1.3)
            x = r*math.cos(math.radians(theta*i))
            y = r*math.sin(math.radians(theta*i))
            point_list.append((x,y))
        return point_list


    def getSpinRate(self):
        return self.mSpinRate

    def setSpinRate(self,spin_rate):
        self.mSpinRate = spin_rate

    def evolve(self,dt):
        self.rotate(self.mSpinRate*dt)
        self.move(dt)
