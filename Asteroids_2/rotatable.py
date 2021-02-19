import movable
import math

class Rotatable(movable.Movable):

    def __init__(self,x,y,dx,dy,rotation,width,height):
        movable.Movable.__init__(self, x,y,dx,dy,width,height)
        self.mRotation = rotation

    def getRotation(self):
        return self.mRotation

    def rotate(self,dr): # dr is for delta_rotation
        self.mRotation = (360 + (self.mRotation + dr)) % 360


    def splitDeltaVIntoXAndY(self,rotation,dv): # dv is for delta_velocity
        new_rotation = rotation*(math.pi/180)

        x = dv * math.cos(new_rotation)
        y = dv * math.sin(new_rotation)
        return (x,y)

    def accelerate(self,dv):
        new_position = self.splitDeltaVIntoXAndY(self.mRotation,dv)

        dx = new_position[0]
        dy = new_position[1]

        self.mDX += dx
        self.mDY += dy


    def rotatePoint(self,x,y):
        # convert to polar
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y,x)

        theta += (self.mRotation*(math.pi/180))
        # convert to cartersan coordinates
        x = r * math.cos(theta)
        y = r * math.sin(theta)
 
        return (x,y)

    def translatePoint(self,x,y):

        x += self.mX
        y += self.mY

        return x,y

    def rotateAndTranslatePoint(self,x,y):

        x,y = self.rotatePoint(x,y)
        x,y = self.translatePoint(x,y)

        return (x,y)

    def rotateAndTranslatePointList(self,point_list):

        new_Point_List = []
        for point in point_list:
            x = point[0]
            y = point[1]
            newpoint = self.rotateAndTranslatePoint(x,y)
            new_Point_List.append(newpoint)

        return new_Point_List
