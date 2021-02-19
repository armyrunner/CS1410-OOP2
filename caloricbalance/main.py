import caloric_balance
import sys


def formatMenu():
    lst =  ['What would you like to do? ', '[f] Record Food Consumption', '[a] Record Physical Activity','[q] Quit ' ]
    return lst

def formatMenuPrompt():
    prompt = 'Enter an option: '
    return prompt

def formatActivityMenu():
    lsta =  ['Choose an activity to record? ', '[j] Jump Rope', '[r] Running','[s] Sitting','[w] Walking']
    return lsta

def getUserString(prompt):
    text = ""
    while len(text) == 0:
        text = input(prompt).strip()
    return text

def getUserFloat(prompt):
    while True:
        try:
            num = getUserString(prompt)
            num = float(num)
            if num <= 0.0:
                print("Value must be greater than zero.")
            else:
                return num
        except:
            print("You Entered a invalid response. Try Again!")

def createCaloricBalance():
    gen = "What is your gender [m] male or [f] female?"
    gender =getUserString(gen)
    a = "What is your age?"
    age = getUserFloat(a)
    h = "What is your height in inches?"
    height = getUserFloat(h)
    w = "What is your weight in pounds?"
    weight = getUserFloat(w)

    cb1 = caloric_balance.CaloricBalance(gender,age,height,weight)
    return cb1


def recordActivityAction(cb1):
    print('Choose an acitvity to record!')
    menu = formatActivityMenu()
    for i in range(len(menu)):
        print(menu[i])
    prompt = formatMenuPrompt()
    activity = getUserString(prompt)
    act = {"jump":.074,"run":.115,"sit":.009,"walk":.036}
    if activity == 'j':
        prompt1 = ' How many minutes did you perform this activity?'
        minutes = getUserFloat(prompt1)
        burn = act["jump"]
        cb1.recordActivity(burn,minutes)
        new = "Awsome! Your caloric balance is now "+str(cb1.getBalance())
        return print(new)
    elif activity == 'r':
        prompt1 = ' How many minutes did you perform this activity?'
        minutes = getUserFloat(prompt1)
        burn = act["run"]
        cb1.recordActivity(burn,minutes)
        new = "Awsome! Your caloric balance is now "+str(cb1.getBalance())
        return print(new)
    elif activity == 's':
        prompt1 = ' How many minutes did you perform this activity?'
        minutes = getUserFloat(prompt1)
        burn = act["sit"]
        cb1.recordActivity(burn,minutes)
        new = "Awsome! Your caloric balance is now "+str(cb1.getBalance())
        return print(new)
    elif activity == 'w':
        prompt1 = ' How many minutes did you perform this activity?'
        minutes = getUserFloat(prompt1)
        burn = act["walk"]
        cb1.recordActivity(burn,minutes)
        new = "Awsome! Your caloric balance is now "+str(cb1.getBalance())
        return print(new)
    else:
        print('Sorry, that option is invalid.')

def eatFoodAction(cb1):
    prompt = 'How many calories did you just eat?'
    cal = getUserFloat(prompt)
    cb1.eatFood(cal)
    new = "Awsome! Your caloric balance is now "+str(cb1.getBalance())
    return print(new)

def quitAction(cb1):
    print("End of Program")
    sys.exit(0)

def applyAction(cb1,choice):
    if choice == "f":
        eatFoodAction(cb1)
    elif choice == "a":
        recordActivityAction(cb1)
    elif choice == "q":
        quitAction(cb1)
    else:
        print("Sorry, that option is invalid!")

def main():
    cb1 = createCaloricBalance()

    while True:

        menu = formatMenu()
        for i in range(len(menu)):
            print(menu[i])

        choice = getUserString(formatMenuPrompt())
        applyAction(cb1,choice)

if __name__ == '__main__':
    main()
