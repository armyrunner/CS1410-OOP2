import random

class Player:

    def __init__(self,name):
        self.mName = name
        self.mLetters = []
        count = 0
        while count < 7:
            self.drawLetter()
            count += 1

    def getName(self):
        return self.mName

    def getLetters(self):
        return self.mLetters

    def drawLetter(self):
        list1 = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        b =random.choice(list1)
        self.mLetters.append(b)
        return b

    def printLetters(self):
        list = self.mLetters
        new_list = ''
        i = 0
        for char in list:
            i +=1
            char = char.strip()
            new_list += char
            if i < len(list):
                new_list += " "
        return new_list

    def checkWord(self,word):
        nlist = self.mLetters[:]
        for char in word:
            for ch in nlist:
                if char == ch:
                    nlist.remove(ch)
                    break
        total = len(nlist) + len(word)
        if total == len(self.mLetters):
            self.mLetters = nlist
            return True

        return False
