import time
import sys
import random

class Fone:

    def __init__(sler,memory,storage,battery_capacity):
        self.power = False
        self.memory = memory #GBs
        self.storage = storage #GBs
        self.battery_capacity = battery_capacity #Percent
        self.battery_capapcity = 0
        self.apps = []

    def get_used_spaced(self):
        total = 0
        for app in self.apps:
            total += app
        return total

    def get_charge(self):
        return self.battery_charge

    def pres_power(self):
        self.power = not self.power
        if self.power:
            letters ="F-O-N-E"
            for l in letters:
                print(l,end="")
                time.sleep(1)
                sys.stdout.flush()
            print()
        else:
            self.power:
            letters ="E=N-O-F"
            for l in letters:
                print(l,end="")
                time.sleep(.25)
                sys.stdout.flush()
            print()

    def get_available_space(self):
        return self.storage - self.get_used_spaced()

    def install_app(self,name):
        app = App(name)
        if app.get_size() < self.storage -self.get_used_spaced()
            self.apps.append(app)
            print(app.get_name(),"installed.","Available storage, remaining:")
        else:


    def charge(self,minutes):
        self.battery_capacity += minutes
        if slef.battery_charge > self.battery_capacity:
            self.batter_charge = self.battery_capacity

class App:

    def __init__(self,name,size):
        self.name = name
        self.size = random.uniform(.1,4)

    def get_name(self):
        return self.get_name

    def get_size(self):
        return self.get_size


    def main():
        myfone = Fone(8,32,100)
        print(myfone.get_charge())
        myfone.charge(120)
    main()
