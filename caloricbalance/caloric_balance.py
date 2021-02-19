class CaloricBalance:

    def __init__(self,gender,age,height,weight):
        self.mWeight = weight
        self.mBalance = -self.getBMR(gender,age,height,self.mWeight)

    def getBMR(self,gender,age,height,weight):
        if gender == 'm':
            men = float(66+((12.7*height) + (6.23*weight)-(6.8*age)))
            return men
        elif gender =='f':
            women = float(655+((4.7*height) + (4.35*weight)-(4.7*age)))
            return women
        else:
            return 0.0

    def getBalance(self):
        return self.mBalance

    def recordActivity(self,caloric_burn_per_pound_per_minute,minutes):
        sum1 = float(caloric_burn_per_pound_per_minute)*float(self.mWeight)
        caloric_burn = sum1*float(minutes)
        self.mBalance = self.mBalance - caloric_burn
        return self.mBalance

    def eatFood(self,calories):
        self.mBalance = self.mBalance + calories
        return self.mBalance
