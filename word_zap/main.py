import player
import sys

g_player_name = []

"""
Programmer: Andrew Nelson
Intial Start: 02/13/219
D#: D00090307
Name of Program: WordZapp. Word game like Banana Grams. First player to use all letters
wins the game.

"""
def formatMenu():
    print(" ")
    lsta =  [' Welcome to WordZapp. How to play the game. Game rules: each player begins the game with\n seven letters. Players take turns eliminating their letters by forming words that\n use their letters (but only their letters), and the first player to eliminate all of\n their letters wins. If a player cannot form a valid word using their letters, they may\n choose to pass their turn and receive an additional letter. Letters are selected randomly\n by the game.','', '[p] PLAY ','[q] QUIT']
    return lsta

def formatMenuPrompt():
    prompt = 'Enter an option: '
    return prompt

def getUserInt(prompt):
    while True:
        try:
            num = getUserString(prompt)
            num = int(num)
            if num <= 0:
                print("Value must be greater than zero.")
            else:
                return num
        except:
            print("You Entered a invalid response. Try Again!")

def getUserString(prompt):
    text = ""
    while len(text) == 0:
        text = input(prompt).strip()
    return text

def convertToLower(word):
    nlist = list_player
    return nlist.lower()

def createPlayers():
    num_players = 'Enter the number of players -> '
    num = getUserInt(num_players)
    for i in range(num):
        print("Player",i +1,"Enter Name:", end = " ")
        name = input("-> ")
        ply = player.Player(name)
        g_player_name.append(ply)

def takePlayerTurn(player):
    print(" ")
    print(player.getName(),", it is your turn")
    print("Your Letters are:",player.printLetters())
    word = input('Enter a word to play (or press enter to pass): ')

    check = player.checkWord(word)
    if check:
        print('Great Job!')
    else:
        print('Try again!')

def gameNotOver(g_player_name):
    for player in g_player_name:
        if len(player.getLetters()) == 0:
            return False
    return True

def quitAction():
    print("End of Program")
    sys.exit(0)

def startGame():

    choice = "x"
    while choice != "p" and choice != "q":
        choice = getUserString(formatMenuPrompt())
        if choice == "x":
            print('Invalid Respone. Please try again!')
        if choice == "q":
            quitAction()
        else:
            createPlayers()
            print("Lets Play WordZapp")


def main():

        menu = formatMenu()
        for i in range(len(menu)):
            print(menu[i])

        startGame()

        while gameNotOver(g_player_name):
            for player in g_player_name:
                takePlayerTurn(player)

        for player in g_player_name:
            if len(player.getLetters()) == 0:
                print(player.getName(),",Congradulations. You Win")
            


if __name__ == '__main__':
    main()