# Made by Brett Wilson
# contact: https://github.com/BrettWilsonBDW
# Made using pyscript: https://pyscript.net/  

import js
import simpleeval as spe

# global lists
numArr = []
sumArr = []

# function to do the sum using simple eval
def calcLogic(numString):
    arrLen = len(sumArr)
    sumString = ''.join(sumArr)

    if (arrLen < 1):
        sumArr.clear()
        output = spe.simple_eval(numString)
        output = str(output)
        sumArr.append(output)
        numArr.clear()
        return output
    else:
        if (not (numArr[0] == "+" or numArr[0] == "-" or numArr[0] == "*" or numArr[0] == "/" or  numArr[0] == "%")):
            output = "syntax error"
            return output
        else:
            sumString = ''.join(sumArr)
            output = spe.simple_eval(sumString + numString)
            output = str(output)
            numArr.clear()
            sumArr.clear()
            sumArr.append(output)
            return output
        

# function to display numbers to the screen of the calculator
def displayCalcOutput(flag = False):
    numString = ''.join(numArr)
    displayArr = []
    prefixAns = ""
    sumArrLen = len(sumArr)
    arrLen = len(numString) 
    i = 0

    while (i < arrLen):
        if (numString[i] == '+'):
            displayArr.append(" + ")
        elif (numString[i] == '-'):
            displayArr.append(" - ")
        elif (numString[i] == '*'):
            displayArr.append(" * ")
        elif (numString[i] == '/'):
            displayArr.append(" / ")
        elif (numString[i] == '%'):
            displayArr.append(" % ")
        else:
            displayArr.append(numString[i])
        i += 1
    
    numDisplay = ''.join(displayArr)

    if (sumArrLen >= 1):
        prefixAns = "ans"
    if (flag == True):
        numDisplay = prefixAns + numDisplay + " = " + str(calcLogic(numString))
    else:
        numDisplay = prefixAns + numDisplay
        
    mainCalcBox = Element("mainCalcDisplay")
    mainCalcBox.write(numDisplay)


# functions that listen for button on the dom
def num1():
    Element('mainCalcDisplay').write("1")
    numArr.append("1")
    displayCalcOutput()


def num2():
    Element('mainCalcDisplay').write("2")
    numArr.append("2")
    displayCalcOutput()


def num3():
    Element('mainCalcDisplay').write("3")
    numArr.append("3")
    displayCalcOutput()


def num4():
    Element('mainCalcDisplay').write("4")
    numArr.append("4")
    displayCalcOutput()


def num5():
    Element('mainCalcDisplay').write("5")
    numArr.append("5")
    displayCalcOutput()


def num6():
    Element('mainCalcDisplay').write("6")
    numArr.append("6")
    displayCalcOutput()


def num7():
    Element('mainCalcDisplay').write("7")
    numArr.append("7")
    displayCalcOutput()


def num8():
    Element('mainCalcDisplay').write("8")
    numArr.append("8")
    displayCalcOutput()


def num9():
    Element('mainCalcDisplay').write("9")
    numArr.append("9")
    displayCalcOutput()


def num0():
    Element('mainCalcDisplay').write("0")
    numArr.append("0")
    displayCalcOutput()


def opPlus():
    Element('mainCalcDisplay').write("+")
    numArr.append("+")
    displayCalcOutput()


def opMinus():
    Element('mainCalcDisplay').write("-")
    numArr.append("-")
    displayCalcOutput()


def opTimes():
    Element('mainCalcDisplay').write("*")
    numArr.append("*")
    displayCalcOutput()


def opDivide():
    Element('mainCalcDisplay').write("/")
    numArr.append("/")
    displayCalcOutput()


def opMod():
    Element('mainCalcDisplay').write("%")
    numArr.append("%")
    displayCalcOutput()

def deleteNum():
    arrLen = len(numArr)

    if (not (arrLen == 0)):
        numArr.pop()
    
    displayCalcOutput()


def clearCalc():
    numArr.clear()
    sumArr.clear()
    arrLen = len(numArr)

    if (arrLen == 0):
        Element('mainCalcDisplay').write(" ")


def calculate():
    numString = ''.join(numArr)
    arrLen = len(numArr)

    if (arrLen == 0):
        Element('mainCalcDisplay').write("Nothing to calculate!")
    elif ("/0" in numString):
        Element('mainCalcDisplay').write("Cannot divide by zero!")
        numArr.clear()
        sumArr.clear()
    elif ("%0" in numString):
        Element('mainCalcDisplay').write("Cannot mod by zero!")
    else:
        displayCalcOutput(True)
