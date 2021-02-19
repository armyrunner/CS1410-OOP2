import polygon
import bullet

class Ship(polygon.Polygon):

    def __init__(self,x,y,width,height):
        dx = 0
        dy = 0
        rotation = 0
        polygon.Polygon.__init__(self,x,y,dx,dy,rotation,width,height)
        p1 = (0,0)
        p2 = (-10,-10)
        p3 = (20,0)
        p4 = (-10,10)
        self.mPoint_list = [p1,p2,p3,p4]
        self.setPolygon(self.mPoint_list)

    
    def fire(self):
      x,y = self.rotateAndTranslatePoint(self.mOriginalPolygon[0][0],self.mOriginalPolygon[0][1])
       
      round = bullet.Bullet(x, y, self.mDX, self.mDY, self.mRotation, self.mWorldWidth, self.mWorldHeight)

      return round
  
    def evolve(self,dt):
        self.move(dt)
