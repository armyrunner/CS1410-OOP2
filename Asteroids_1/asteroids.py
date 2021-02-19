import rock
import ship
import pygame
import random


class Asteroids:

    def __init__(self,width,height):
        self.mWorldWidth = width
        self.mWorldHeight = height

        shipx = random.randint(0,self.mWorldWidth)
        shipy = random.randint(0,self.mWorldHeight)

        self.mColorObject = (255,255,255)
        self.mShip = ship.Ship(shipx,shipy,self.mWorldWidth,self.mWorldHeight)

        NUM_ROCKS = random.randint(10,20)
        self.mRocks = []
        for i in range(NUM_ROCKS):
            rockx = random.randint(0,self.mWorldWidth)
            rocky = random.randint(0,self.mWorldHeight)
            rocks = rock.Rock(rockx,rocky,self.mWorldWidth,self.mWorldHeight)
            self.mRocks.append(rocks)

        self.mObjects = self.mRocks + [self.mShip]

    def getWorldHeight(self):
        return self.mWorldHeight

    def getWorldWidth(self):
        return self.mWorldWidth

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getObjects(self):
        return self.mObjects

    def turnShipLeft(self,delta_rotation):
        self.mShip.rotate(-delta_rotation)

    def turnShipRight(self,delta_rotation):
        self.mShip.rotate(delta_rotation)

    def accelerateShip(self,delta_velocity):
        self.mShip.accelerate(delta_velocity)

    def evolve_all_objects(self,dt):
        for object_list in self.mObjects:
            object_list.evolve(dt)

    def evolve(self,dt):
        self.evolve_all_objects(dt)
        
    def draw(self,surface):
        surface.fill((0,0,0))
        for objects in self.mObjects:
            objects.draw(surface)
