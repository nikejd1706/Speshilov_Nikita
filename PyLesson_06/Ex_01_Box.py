string = input("Please enter a string: ")

def printString():
    for i in range(0, len(string)):
        print(string[i:len(string)])
printString()
