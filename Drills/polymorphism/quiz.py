import multiplicationproblem
import additionproblem
import random


def make_problems(min_value,max_value,num_problems):

    problems = []

    for i in range(num_problems):
        problems.append(create_problem(min_value,max_value))

    return problems

def create_problem(min_value,max_value):

     l = random.randrange(min_value,max_value+1)
     r = random.randrange(min_value,max_value+1)

     if random.randint(1,2) == 1:
         return additionproblem.AdditionProblem(l,r)

     else:
         return multiplicationproblem.MultiplicationProblem(l,r)

def check_problems(problems,answers):
     count = 0
     for i in range(len(problems)):
         if problems[i].checkAnswer(answers[i]):
            count += 1
     return count
