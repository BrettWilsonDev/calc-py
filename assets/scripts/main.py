# Made by Brett Wilson
# contact: https://github.com/BrettWilsonBDW
# Made using pyscript: https://pyscript.net/  


import js
import simpleeval as spe
import re

numArr = []


def calcLogic(numString):
    output = spe.simple_eval(numString)
    return output


def displayCalcOutput(numString):
    displayArr = []

    i = 0
    arrLen = len(numString)
    while (i < arrLen):
        if numString[i] == '+':
            displayArr.append(" + ")
        elif numString[i] == '-':
            displayArr.append(" - ")
        elif numString[i] == '*':
            displayArr.append(" * ")
        elif numString[i] == '/':
            displayArr.append(" / ")
        elif numString[i] == '%':
            displayArr.append(" % ")
        else:
            displayArr.append(numString[i])

        i += 1

    numDisplay = ''.join(displayArr)
    numDisplay = numDisplay + " = " + str(calcLogic(numString))
    mainCalcBox = Element("mainCalcDisplay")
    mainCalcBox.write(numDisplay)
      

def num1():
    Element('mainCalcDisplay').write("1")
    numArr.append("1")


def num2():
    Element('mainCalcDisplay').write("2")
    numArr.append("2")


def num3():
    Element('mainCalcDisplay').write("3")
    numArr.append("3")


def num4():
    Element('mainCalcDisplay').write("4")
    numArr.append("4")


def num5():
    Element('mainCalcDisplay').write("5")
    numArr.append("5")


def num6():
    Element('mainCalcDisplay').write("6")
    numArr.append("6")


def num7():
    Element('mainCalcDisplay').write("7")
    numArr.append("7")


def num8():
    Element('mainCalcDisplay').write("8")
    numArr.append("8")


def num9():
    Element('mainCalcDisplay').write("9")
    numArr.append("9")


def num0():
    Element('mainCalcDisplay').write("0")
    numArr.append("0")


def opPlus():
    Element('mainCalcDisplay').write("+")
    numArr.append("+")


def opMinus():
    Element('mainCalcDisplay').write("-")
    numArr.append("-")


def opTimes():
    Element('mainCalcDisplay').write("*")
    numArr.append("*")


def opDivide():
    Element('mainCalcDisplay').write("/")
    numArr.append("/")


def opMod():
    Element('mainCalcDisplay').write("%")
    numArr.append("%")


def clearCalc():
    numArr.clear()
    arrLen = len(numArr)
    if (arrLen == 0):
        Element('mainCalcDisplay').write(" ")



def calculate():
    numString = ''.join(numArr)
    arrLen = len(numArr)

    if (arrLen == 0):
        Element('mainCalcDisplay').write("Nothing to calculate!")
    elif "/0" in numString:
        Element('mainCalcDisplay').write("Cannot divide by zero!")
    elif "%0" in numString:
        Element('mainCalcDisplay').write("Cannot mod by zero!")
    else:
        numString = ''.join(numArr)
        calcLogic(numString)
        displayCalcOutput(numString)


# def calcIn():
#     input_box = Element("calc_input")
#     calcOut = input_box.value
#     mainCalcBox = Element("calcBox")
#     mainCalcBox.write(calcOut)

