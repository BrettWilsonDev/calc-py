# Made by Brett Wilson
# contact: https://github.com/BrettWilsonBDW
# Made using pyscript: https://pyscript.net/  

import js
import simpleeval as spe
import re

numArr = []
sumArr = []


def calcLogic(numString, op):
    arrLen = len(sumArr)
    if (arrLen < 1):
        sumArr.clear()
        output = spe.simple_eval(numString)
        output = str(output)
        sumArr.append(output)
        numArr.clear()
        return output
    else:
        sumString = ''.join(sumArr)
        output = spe.simple_eval(sumString + numString)
        # print(f"op: {op} sumString: {sumString} numString: {numString} numArr: {numArr} sumArr: {sumArr} total = {sumString + numString}")
        output = str(output)
        # reset numArr and SumArr as well add current value to now free slot in sumArr
        numArr.clear()
        sumArr.clear()
        sumArr.append(output)
        return output
        

def displayCalcOutput(flag = False):
    numString = ''.join(numArr)
    displayArr = []
    sumArrLen = len(sumArr) 
    prefixAns = ""

    i = 0
    arrLen = len(numString)
    while (i < arrLen):
        if (numString[i] == '+'):
            displayArr.append(" + ")
            op = "+"
        elif (numString[i] == '-'):
            displayArr.append(" - ")
            op = "-"
        elif (numString[i] == '*'):
            displayArr.append(" * ")
            op = "*"
        elif (numString[i] == '/'):
            displayArr.append(" / ")
            op = "/"
        elif (numString[i] == '%'):
            displayArr.append(" % ")
            op = "%"
        else:
            displayArr.append(numString[i])
        i += 1

    if (sumArrLen >= 1):
        prefixAns = "ans"

    numDisplay = ''.join(displayArr)
    if (flag == True):
        numDisplay = prefixAns + numDisplay + " = " + str(calcLogic(numString, op))
    else:
        numDisplay = prefixAns + numDisplay
        
    mainCalcBox = Element("mainCalcDisplay")
    mainCalcBox.write(numDisplay)


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
    elif "/0" in numString:
        Element('mainCalcDisplay').write("Cannot divide by zero!")
        numArr.clear()
        sumArr.clear()
    elif "%0" in numString:
        Element('mainCalcDisplay').write("Cannot mod by zero!")
    else:
        displayCalcOutput(True)


