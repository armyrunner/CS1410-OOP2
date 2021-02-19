import sys

def milesPerGallon(miles, gallons):

    miles = float(miles)
    gallons = float(gallons)

    if gallons == 0.0:
        return 0.0
    else:
        total = miles/gallons
        return total

def createNotebook():
    notebook = []
    return notebook

def recordTrip(notebook,date,miles,gallons):
    #create dictionary
    trip = {}
    # change all values to decimal
    miles = float(miles)
    gallons = float(gallons)
    # key and values for dicitonary
    trip["date"] = date
    trip["miles"] = miles
    trip["gallons"] = gallons

    notebook.append(trip)

def listTrips(notebook):
    strlist = []

    for items in notebook:
        mpg = milesPerGallon(items["miles"],items["gallons"])
        strlist.append("On "+items["date"]+" : "+str(items["miles"])+" miles traveled using "+str(items["gallons"])+" gallons. Gas milage: "+str(mpg)+" MPG")
    return strlist

def calculateMPG(notebook):

    sum_miles = 0
    sum_gallons = 0

    for items in notebook:

        sum_miles += items["miles"]
        sum_gallons += items["gallons"]

    if sum_miles == 0.0 or sum_gallons == 0.0:
        return 0.0
    else:
        average = sum_miles/sum_gallons
        return average

def formatMenu():
    lst =  ['What would you like to do? ', '[r] Record Gas Consumption', '[l] List Milage History', '[c] Calcuate Gas Milage', '[q] Quit ' ]
    return lst


def formatMenuPrompt():
    prompt = 'Enter an option: '
    return prompt

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

def getDate():
    prompt = "What is the Date? "
    user = getUserString(prompt)
    return user

def getMiles():
    prompt = "How many miles did you travel since last fill up? "
    user = getUserFloat(prompt)
    return user

def getGallons():
    prompt = "How many gallons did you add to your tank? "
    user = getUserFloat(prompt)
    return user

def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()


    if len(date) > 0 and miles > 0.0 and gallons > 0.0:
        recordTrip(notebook,date,miles,gallons)
        print("Trip was Saved")
    else:
        print("Trip was Not Saved")

def listTripsAction(notebook):
     trip = listTrips(notebook)

     for items in trip:
        print(items)

     if len(trip) == 0:
         print("No Trips have been recorded!")

def calculateMPGAction(notebook):
    average = calculateMPG(notebook)
    if average == 0:
        print("No Trips have been recorded!")
    else:
        answer = "Average gas milage: "+ str(round(average,2))+ " MPG"
        print(answer)

def quitAction(notebook):
    print("End of Program")
    sys.exit(0)

def applyAction(notebook,choice):
    if choice == "r":
        recordTripAction(notebook)
    elif choice == "l":
        listTripsAction(notebook)
    elif choice == "c":
        calculateMPGAction(notebook)
    elif choice == "q":
        quitAction(notebook)
    else:
        print("Sorry, that option is invalid!")

def main():
    trip = createNotebook()

    while True:

        menu = formatMenu()
        for i in range(len(menu)):
            print(menu[i])

        choice = getUserString(formatMenuPrompt())
        applyAction(trip,choice)

if __name__ == '__main__':
    main()
