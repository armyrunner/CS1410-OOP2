import mathproblem

class MultiplicationProblem(mathproblem.MathProblem):

    def __init__(self,lhs, rhs):
        mathproblem.MathProblem.__init__(self,lhs,rhs)
        self.operator = "*"

    def getString(self):
        self.string = str(self.lhs) + " * " + str(self.rhs)
        return self.string

    def checkAnswer(self,ans):
        multi = self.lhs * self.rhs
        if ans == multi:
            return True
        return False
