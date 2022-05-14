def getInput():
    string = input("Enter number ")
    return string


def testInput(string):
    return string.isdigit()


def strToInt(string):
    return int(string)


def printInt(number):
    print(number)


input_string = getInput()

if testInput(input_string):
    number = strToInt(input_string)
    printInt(number)

