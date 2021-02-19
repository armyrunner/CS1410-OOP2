import sys

def createIndex():
    isbndict = {}
    return isbndict


def recordBook(index, isbn, title):

        index[isbn]=title


def findBook(index,isbn):
    empty_string = ""

    if isbn not in index:
        return empty_string

    else:
        return index[isbn]


def listBooks(index):
    book = []
    count = 1

    for item in index:

        if len(index) > 0:
            lst = str(count)+")"+item+":"+index[item]
            book.append(lst)
            count += 1
        else:
            return book

    return book


def formatMenu():
    lst =  ['What would you like to do? ', '[r] Record a book', '[f] Find a Book', '[l] List all Books', '[q] Quit ' ]
    return lst


def formatMenuPrompt():
    choice = 'Enter an option: '
    return choice


def getUserChoice(prompt):

    text = ""

    while len(text) == 0:

        text = input(prompt).strip()

    return text


def getISBN():

    user = getUserChoice("Enter an International Standard Book Number(ISBN): ")

    return user


def getTitle():

    title = getUserChoice("Enter Book title: ")

    return title


def recordBookAction(index):

    isbn = getISBN()
    title = getTitle()

    recordBook(index,isbn,title)


def findBookAction(index):

     isbn = getISBN()

     if isbn in index.keys():
         print("Book Found: ",index[isbn])
     else:
         print("The Book Does Not Exist!")


def listBooksAction(index):

     books = listBooks(index)

     for book in books:
        print(book)

     if len(books) == 0:
         print("No Books Exist: ")

def quitAction(index):
    print("End of Program")
    sys.exit(0)


def applyAction(index,choice):

    if choice == "r":
        recordBookAction(index)
    elif choice == "f":
        findBookAction(index)
    elif choice == "l":
        listBooksAction(index)
    elif choice == "q":
        quitAction(index)
    else:
        print("Sorry, that option is invalid!")

def main():

    index = createIndex()

    while True:

        menu = formatMenu()
        for i in range(len(menu)):
            print(menu[i])

        choice = getUserChoice(formatMenuPrompt())
        applyAction(index,choice)


if __name__ == '__main__':
    main()

