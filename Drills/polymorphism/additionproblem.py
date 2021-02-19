import mathproblem


class AdditionProblem(mathproblem.MathProblem):

    def __init__(self, lhs, rhs):
        mathproblem.MathProblem.__init__(self, lhs, rhs)
        self.operator = "+"

    def getString(self):
        self.string = str(self.getLHS()) + " + " + str(self.getRHS())
        return self.string

    def checkAnswer(self, ans):
        if (self.getLHS() + self.getRHS()) == ans:
            return True
        else:
            return False
