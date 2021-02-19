import rock
import ship
import bullet
import star
import pygame
import random


MAX_ACTIVE_BULLET = 3


class Asteroids:

    def __init__(self,width,height):
        self.mWorldWidth = width
        self.mWorldHeight = height

        shipx = random.randint(0,self.mWorldWidth)
        shipy = random.randint(0,self.mWorldHeight)

        self.mShip = ship.Ship(shipx,shipy,self.mWorldWidth,self.mWorldHeight)

        self.mBullet = []

        NUM_ROCKS = random.randint(10,20)
        self.mRocks = []
        for i in range(NUM_ROCKS):
            rockx = random.randint(0,self.mWorldWidth)
            rocky = random.randint(0,self.mWorldHeight)
            rocks = rock.Rock(rockx,rocky,self.mWorldWidth,self.mWorldHeight)
            self.mRocks.append(rocks)

        NUM_STARS = 20
        self.mStars = []
        for i in range(NUM_STARS):
            starsx = random.randint(0,self.mWorldWidth)
            starsy = random.randint(0,self.mWorldHeight)
            stars = star.Star(starsx,starsy,self.mWorldWidth,self.mWorldHeight)
            self.mStars.append(stars)

        self.mObjects = self.mRocks[:] + [self.mShip] + self.mStars[:]

    def getWorldHeight(self):
        return self.mWorldHeight

    def getWorldWidth(self):
        return self.mWorldWidth

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getStars(self):
        return self.mStars

    def getBullets(self):
        return self.mBullet

    def getObjects(self):
        return self.mObjects

    def fire(self):

        if len(self.mBullet) != 3:
            firex = self.mShip.mX
            firey = self.mShip.mY
            firerotation = self.mShip.mRotation
            firedx = self.mShip.mDX
            firedy = self.mShip.mDY
            fire_round = bullet.Bullet(firex,firey,firedx,firedy,firerotation,self.mWorldWidth,self.mWorldHeight)
            self.mBullet.append(fire_round)
            self.mObjects.append(fire_round)


    def turnShipLeft(self,delta_rotation):
        self.mShip.rotate(-delta_rotation)

    def turnShipRight(self,delta_rotation):
        self.mShip.rotate(delta_rotation)

    def accelerateShip(self,delta_velocity):
        self.mShip.accelerate(delta_velocity)

    def evolveAllObjects(self,dt):
        for object_list in self.mObjects:
            object_list.evolve(dt)

    def collideShipAndBullets(self):
        for bullets in self.mBullet:
            if bullets.hits(self.mShip):
                bullets.mActive = False
                self.mShip.mActive = False

    def collideShipAndRocks(self):
        for rocks in self.mRocks:
            if rocks.hits(self.mShip):
                rocks.mActive = False
                self.mShip.mActive = False

    def collideRocksAndBullets(self):
        for bullets in self.mBullet:
            for rocks in self.mRocks:
                if rocks.mActive and bullets.mActive:
                    if bullets.hits(rocks):
                        bullets.mActive = False
                        rocks.mActive = False

    def removeInactiveObjects(self):
        for objects in self.mObjects:
            if not objects.mActive:
                self.mObjects.remove(objects)
        for objects in self.mBullet:
            if not objects.mActive:
                self.mBullet.remove(objects)
        for rocks in self.mRocks:
            if not rocks.mActive:
                self.mRocks.remove(rocks)

    def evolve(self,dt):
        self.evolveAllObjects(dt)
        self.collideRocksAndBullets()
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.removeInactiveObjects()

    def draw(self,surface):
        surface.fill((0,0,0))
        for objects in self.mObjects:
            if objects.mActive:
                objects.draw(surface)
