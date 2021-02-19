import pygame
import random
from froggerlib import Frog
from froggerlib import Stage
from froggerlib import road
from froggerlib import car
from froggerlib import race_car
from froggerlib import dozer
from froggerlib import truck
from froggerlib import water
from froggerlib import home
from froggerlib import grass
from froggerlib import log
from froggerlib import turtle



class Frogger:

    def __init__( self,NUM_COLS,NUM_ROWS,CELL_SIZE ):

        self.mColumns = NUM_COLS
        self.mRows = NUM_ROWS
        self.mCell_size = CELL_SIZE
        self.mScreenWidth = NUM_COLS*CELL_SIZE
        self.mScreenHeight =NUM_ROWS*CELL_SIZE
        self.mGameOver = False
        self.mFrogwins = False
        self.mCarColor = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        self.mDozerColor = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        self.mRaceCarColor = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        self.mTruckColor = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        # self.mHomeColor = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        gapsize = .1 #spacing multiplier
        self.mObjWidth = CELL_SIZE-(2*gapsize*self.mCell_size)# width of objects
        self.mObjHeight= CELL_SIZE-(2*gapsize*self.mCell_size)# height of objects   

        # for frog
        hg = CELL_SIZE# horizontal gap
        vg = CELL_SIZE # vertical gap
        num_lanes = 4 # number of roads/ water ways
        num_cars = 3# number of cars per lane
        num_racecar = 1
        num_home_area = 3
        frogx = .5*self.mScreenWidth # frog position
        frogy = (self.mRows - 1) * self.mCell_size + (self.mCell_size*gapsize) # frog position
        dx = frogx # desired x
        dy = frogy # desired y
        speed = 10
        self.mFrog = Frog(frogx,frogy,self.mObjWidth,self.mObjHeight,dx,dy,speed,hg,vg )

        # safe place for frog
        self.mStage1 = Stage(0,(self.mRows-1)*self.mCell_size,self.mScreenWidth,self.mScreenHeight)
        self.mStage2 = Stage(0,(self.mRows-6)*self.mCell_size,self.mScreenWidth,self.mCell_size)

        # Avoid area
        grassX = 0
        grassY = (self.mRows-12)*self.mCell_size + self.mCell_size
        grassWidth = self.mScreenWidth
        grassHeight = self.mCell_size
        self.mGrass = grass.Grass(grassX,grassY,grassWidth,grassHeight)


        self.mHome = []
        area = (self.mScreenWidth//3)
        for i in range(num_home_area):
            homeX = area*i+100
            homeY = (self.mRows-12)*self.mCell_size + self.mCell_size
            homeWidth = self.mObjWidth*2
            homeHeight = self.mCell_size
            mHome = home.Home(homeX,homeY,homeWidth,homeHeight)
            self.mHome.append(mHome)


        # # road to cross
        self.mRoad = []
        for i in range(num_lanes):
            roadX = 0
            roadY = (self.mRows-2-i)*self.mCell_size
            roadWidth = self.mScreenWidth
            roadHeight = self.mCell_size
            roadways = road.Road(roadX,roadY,roadWidth,roadHeight)
            self.mRoad.append(roadways)

        # water crossing not touchable
        self.mWater = []
        for i in range(num_lanes):
            waterX = 0
            waterY = (self.mRows-7-i)*self.mCell_size
            waterWidth = self.mScreenWidth
            waterHeight = self.mCell_size
            waterlanes = water.Water(waterX,waterY,waterWidth,waterHeight)
            self.mWater.append(waterlanes)

        self.mCars = []
        # Cars
        for i in range(num_cars):
            carx = (self.mColumns-13)*(self.mCell_size)
            cary = (self.mRows-2)*(self.mCell_size+8*gapsize)
            carwidth =  self.mObjWidth*2
            carheight = self.mObjHeight-(self.mCell_size*gapsize)
            cardx = self.mScreenWidth
            cardy = cary
            carspeed = 10
            carsForRoad = car.Car(carx+(i*150),cary,carwidth,carheight,cardx,cardy,carspeed)
            self.mCars.append(carsForRoad)

        #Dozer
        self.mDozers = []
        for i in range(num_cars):
            dozerx = (self.mColumns-13)*(self.mCell_size) # x position
            dozery = (self.mRows-3)*(self.mCell_size+8*gapsize) # y position
            dozerdx = 2*self.mObjWidth*gapsize - self.mCell_size # desired x position
            dozerdy = dozery
            dozerwidth = self.mObjWidth*2
            dozerheight = self.mObjHeight-(self.mCell_size*gapsize)
            dozerspeed = 2
            dozercars = dozer.Dozer(dozerx+(i*200),dozery,dozerwidth,dozerheight,dozerdx,dozerdy,dozerspeed)
            self.mDozers.append(dozercars)


        #RaceCar
        self.mRace_Car = []
        for i in range(num_racecar):
            racecarx = (self.mColumns-2)*self.mObjWidth
            racecary = (self.mRows-4)*(self.mCell_size+8*gapsize)
            racecarwidth = self.mObjWidth*2
            racecarheight = self.mObjHeight-(self.mCell_size*gapsize)
            racecardx = self.mScreenWidth
            racecardy =  racecary
            minracespeed = 10
            maxracespeed = 30
            fastcar = race_car.RaceCar(racecarx+(i*100),racecary,racecarwidth,racecarheight,racecardx,racecardy,minracespeed,maxracespeed)
            self.mRace_Car.append(fastcar)

        # Truck
        self.mTrucks = []
        for i in range(num_cars):
            truckx = (self.mColumns-13)*(self.mCell_size)
            trucky = (self.mRows-5)*(self.mCell_size+8*gapsize)
            truckwidth = self.mObjWidth*2
            truckheight = self.mObjHeight-(self.mCell_size*gapsize)
            truckdx = self.mObjWidth*gapsize - self.mCell_size
            truckdy = trucky
            truckspeed = 5
            bigtrucks = truck.Truck(truckx+(i*175),trucky,truckwidth,truckheight,truckdx,truckdy,truckspeed)
            self.mTrucks.append(bigtrucks)

        # Logs
        self.mLogs1 = []
        for i in range(num_cars):
            logx = (self.mColumns-13)*(self.mCell_size)
            logy = (self.mRows-7)*(self.mCell_size+8*gapsize)
            logwidth = (self.mCell_size*gapsize) + self.mCell_size
            logheight = self.mObjHeight-(self.mCell_size*gapsize)
            logdx = self.mObjWidth*gapsize - self.mCell_size
            logdy = logy
            logspeed = 5
            floatlogs = log.Log(logx+(i*300),logy,logwidth,logheight,logdx,logdy,logspeed)
            self.mLogs1.append(floatlogs)

        #Turtles
        self.mTurtle1 = []
        for i in range(num_cars):
            turtlex = (self.mColumns-13)*(self.mCell_size)
            turtley = (self.mRows-8)*(self.mCell_size+8*gapsize)
            turtlewidth = self.mObjWidth + (self.mCell_size*gapsize) + self.mCell_size
            turtleheight = self.mObjHeight-(self.mCell_size*gapsize)
            turtledx = self.mObjWidth*gapsize - self.mCell_size
            turtledy = turtley
            turtlespeed = 5
            slowpokes = turtle.Turtle(turtlex+(i*125),turtley,turtlewidth,turtleheight,turtledx,turtledy,turtlespeed)
            self.mTurtle1.append(slowpokes)

        self.mLogs2 = []
        for i in range(num_cars):
            logx = (self.mColumns-13)*(self.mCell_size)
            logy = (self.mRows-9)*(self.mCell_size+8*gapsize)
            logwidth = self.mObjWidth*2 +(self.mCell_size*gapsize)+self.mCell_size
            logheight = self.mObjHeight-(self.mCell_size*gapsize)
            logdx = self.mScreenWidth
            logdy = logy
            logspeed = 5
            floatlogs = log.Log(logx+(i*175),logy,logwidth,logheight,logdx,logdy,logspeed)
            self.mLogs2.append(floatlogs)


        self.mTurtle2 = []
        for i in range(num_cars):
            turtlex = (self.mColumns-13)*(self.mCell_size)
            turtley = (self.mRows-10)*(self.mCell_size+8*gapsize)
            turtlewidth = self.mObjWidth*2 +(self.mCell_size*gapsize)+self.mCell_size
            turtleheight = self.mObjHeight-(self.mCell_size*gapsize)
            turtledx = self.mScreenWidth
            turtledy =  turtley
            turtlespeed = 5
            seacreatures = turtle.Turtle(turtlex+(i*300),turtley,turtlewidth,turtleheight,turtledx,turtledy,turtlespeed)
            self.mTurtle2.append(seacreatures)



# ---------------------------------move the circles to the left side of the window every time the a button is pressed------------------------------------
    def actOnPressUP( self ):
        self.mFrog.up()
        return
    def actOnPressDOWN( self ):
        self.mFrog.down()
        return
    def actOnPressLEFT( self ):
        self.mFrog.left()
        return
    def actOnPressRIGHT( self ):
        self.mFrog.right()
        return

    def evolve(self,dt):
        if self.mGameOver:
            return

        self.mFrog.move()
        if self.mFrog.outOfBounds(self.mScreenWidth,self.mScreenHeight):
            if self.mScreenWidth <= 0 or self.mScreenWidth-self.mObjWidth >= 0:
                self.mGameOver = True
            if self.mScreenHeight - self.mObjHeight >=0:
                self.mGameOver = True

        if self.mGrass.hits(self.mFrog):
           self.mGameOver = True

        for homearea in self.mHome:
            if homearea.hits(self.mFrog):
                self.mFrog.setX(self.mScreenWidth*.5)
                self.mFrog.setDesiredX(self.mScreenWidth*.5)
                self.mFrog.setY((self.mRows - 1) * self.mCell_size + (self.mCell_size*.1))
                self.mFrog.setDesiredY((self.mRows - 1) * self.mCell_size + (self.mCell_size*.1))
                self.mFrogwins = True

        for waterlanes in self.mWater:
            if waterlanes.hits(self.mFrog):
                self.mGameOver = True

        # normal car
        for vehicles in self.mCars:
            vehicles.move()
            if vehicles.atDesiredLocation():
                vehicles.setX(-self.mObjWidth*2)
            if vehicles.hits(self.mFrog):
                self.mGameOver = True

        # Dozer
        for bigtrucks in self.mDozers:
            bigtrucks.move()
            if bigtrucks.atDesiredLocation():
                bigtrucks.setX(self.mScreenWidth+1)
            if bigtrucks.hits(self.mFrog):
                self.mGameOver = True

        for fastcar in self.mRace_Car:
            fastcar.move()
            if fastcar.atDesiredLocation():
                fastcar.setX(-self.mObjWidth*2)
            if fastcar.hits(self.mFrog):
                self.mGameOver = True

        for slowtrucks in self.mTrucks:
            slowtrucks.move()
            if slowtrucks.atDesiredLocation():
                slowtrucks.setX(self.mScreenWidth+1)
            if slowtrucks.hits(self.mFrog):
                self.mGameOver = True

        for logs in self.mLogs1:
            logs.move()
            if logs.atDesiredLocation():
                logs.setX(self.mScreenWidth)
            logs.supports(self.mFrog)

        for logs in self.mLogs2:
            logs.move()
            if logs.atDesiredLocation():
                logs.setX(-self.mObjWidth*2)
            logs.supports(self.mFrog)

        for creatures in self.mTurtle1:
            creatures.move()
            if creatures.atDesiredLocation():
                creatures.setX(self.mScreenWidth)
            creatures.supports(self.mFrog)

        for creature in self.mTurtle2:
            creature.move()
            if creature.atDesiredLocation():
                creature.setX(-self.mObjWidth*2)
            creature.supports(self.mFrog)

#--------------------------------------draw function for the objects------------------------------------------------------------
    def drawFrog(self,surface):
        color =  (0,128,0)
        rect = pygame.Rect(int(self.mFrog.getX()),int(self.mFrog.getY()+2),int(self.mFrog.getWidth()),int(self.mFrog.getHeight()))
        pygame.draw.rect(surface,color,rect,0)

    def drawStage(self,surface):
        color1 =  (192,192,192)
        color2 =  (244,164,96)
        rect = pygame.Rect(int(self.mStage1.getX()),int(self.mStage1.getY()),int(self.mStage1.getWidth()+self.mStage1.getX()),int(self.mStage1.getHeight()+self.mStage1.getY()))
        pygame.draw.rect(surface,color1,rect,0)

        rect = pygame.Rect(int(self.mStage2.getX()),int(self.mStage2.getY()),int(self.mStage2.getWidth()),int(self.mStage2.getHeight()))
        pygame.draw.rect(surface,color2,rect,0)

    def drawRoad(self,surface):
        color = (76, 76, 76)
        color2 = (250,250,250)

        for road_ways in self.mRoad:
            roadways = pygame.Rect(int(road_ways.getX()),int(road_ways.getY()),int(road_ways.getWidth()),int(road_ways.getHeight()))
            pygame.draw.rect(surface,color,roadways,0)

        for roads in self.mRoad:
            rectw1 = pygame.Rect(int(roads.getX()),int(roads.getY()),int(roads.getWidth()),int(roads.getHeight()))
            pygame.draw.rect(surface,color2,rectw1,1)

    def drawGrassArea(self,surface):
           color = (0,128,0)
           rect1 = pygame.Rect(int(self.mGrass.getX()),int(self.mGrass.getY()),int(self.mGrass.getWidth()),int(self.mGrass.getHeight()))
           pygame.draw.rect(surface,color,rect1,0)

    def drawHomeArea(self,surface):
           color = (100,50,110)
           for homearea in self.mHome:
               rect = pygame.Rect(int(homearea.getX()),int(homearea.getY()),int(homearea.getWidth()),int(homearea.getHeight()))
               pygame.draw.rect(surface,color,rect,0)

    def drawWater(self,surface):
        color = (0, 119, 190)
        for water_lanes in self.mWater:
            w = pygame.Rect(int(water_lanes.getX()),int(water_lanes.getY()),int(water_lanes.getWidth()),int(water_lanes.getHeight()))
            pygame.draw.rect(surface,color,w,0)

    def drawCar(self,surface):
        for normcars in self.mCars:
            rect = pygame.Rect(normcars.getX(),normcars.getY(),normcars.getWidth(),normcars.getHeight())
            pygame.draw.rect(surface,self.mCarColor,rect,0)

    def drawDozer(self,surface):
        for largetrucks in self.mDozers:
            rect = pygame.Rect(int(largetrucks.getX()),int(largetrucks.getY()),int(largetrucks.getWidth()),int(largetrucks.getHeight()))
            pygame.draw.rect(surface,self.mDozerColor,rect,0)

    def drawRaceCar(self,surface):
        for speedcar in self.mRace_Car:
            rect = pygame.Rect(int(speedcar.getX()),int(speedcar.getY()),int(speedcar.getWidth()),int(speedcar.getHeight()))
            pygame.draw.rect(surface,self.mRaceCarColor,rect,0)

    def drawTruck(self,surface):
        for bigtrucks in self.mTrucks:
            rect = pygame.Rect(int(bigtrucks.getX()),int(bigtrucks.getY()),int(bigtrucks.getWidth()),int(bigtrucks.getHeight()))
            pygame.draw.rect(surface,self.mTruckColor,rect,0)

    def drawLogs(self,surface):
        color1 = (193,154,107)
        color2 = (141,97,66)
        for ridelogs in self.mLogs1:
            rect = pygame.Rect(int(ridelogs.getX()),int(ridelogs.getY()),int(ridelogs.getWidth()),int(ridelogs.getHeight()))
            pygame.draw.rect(surface,color1,rect,0)

        for ride in self.mLogs2:
            rect = pygame.Rect(int(ride.getX()),int(ride.getY()),int(ride.getWidth()),int(ride.getHeight()))
            pygame.draw.rect(surface,color2,rect,0)

    def drawTurtles(self,surface):
        color1 = (137,178,151)
        color2 = (70,91,78)
        for rideturtle in self.mTurtle1:
            rect = pygame.Rect(int(rideturtle.getX()),int(rideturtle.getY()),int(rideturtle.getWidth()),int(rideturtle.getHeight()))
            pygame.draw.rect(surface,color1,rect,0)

        for rider in self.mTurtle2:
            rect = pygame.Rect(int(rider.getX()),int(rider.getY()),int(rider.getWidth()),int(rider.getHeight()))
            pygame.draw.rect(surface,color2,rect,0)

#-------------------------------------------- draws the current state of the system----------------------------------------------------
    def draw( self, surface ):
         # draws the background
        surface.fill((0,0,0))
        self.drawRoad(surface)
        self.drawStage(surface) # draws stage1
        self.drawCar(surface)
        self.drawDozer(surface)
        self.drawTruck(surface)
        self.drawRaceCar(surface)
        self.drawWater(surface)
        self.drawGrassArea(surface)
        self.drawHomeArea(surface)
        self.drawLogs(surface)
        self.drawTurtles(surface)
        self.drawFrog(surface) # draws the Frog

        return
