import pygame
import sky
import ground
import mountain
import moon
import water
import house
import cloud
import bird

class Picture:


    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mBlueSky = sky.Sky(self.mWidth,self.mHeight)
        self.mGround = ground.Ground(self.mWidth,self.mHeight)
        self.mMountain = mountain.Mountain(self.mWidth,self.mHeight)
        self.mMoon = moon.Moon(self.mWidth,self.mHeight)
        self.mWater = water.Water(self.mWidth,self.mHeight)
        self.mHouse = house.House(self.mWidth,self.mHeight)
        self.mCloud = cloud.Cloud(self.mWidth,self.mHeight)
        self.mBird = bird.Bird(self.mWidth,self.mHeight)

    def evolve(self,dt):
        return

    def draw(self,surface):
        self.mBlueSky.draw(surface)
        self.mMoon.draw(surface)
        self.mMountain.draw(surface)
        self.mGround.draw(surface)
        self.mHouse.draw(surface)
        self.mWater.draw(surface)
        self.mCloud.draw(surface)
        self.mBird.draw(surface)

        return
