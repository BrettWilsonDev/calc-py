# made by Brett Wilson
# https://github.com/BrettWilsonBDW


import js
import simpleeval as spe
import re

numbers = []

def calcLogic(num):
    output = spe.simple_eval(num)
    print(output)
      

def num1():
    Element('show1').write("1")
    numbers.append("1")

def num2():
    Element('show2').write("2")
    numbers.append("2")

def num3():
    Element('show3').write("3")
    numbers.append("3")

def num4():
    Element('show4').write("4")
    numbers.append("4")

def num5():
    Element('show5').write("5")
    numbers.append("5")

def num6():
    Element('show6').write("6")
    numbers.append("6")

def num7():
    Element('show7').write("7")
    numbers.append("7")

def num8():
    Element('show8').write("8")
    numbers.append("8")

def num9():
    Element('show9').write("9")
    numbers.append("9")

def num0():
    Element('show0').write("0")
    numbers.append("0")

def opPlus():
    Element('showPlus').write("+")
    numbers.append("+")

def opMinus():
    Element('showMinus').write("-")
    numbers.append("-")

def opDivide():
    Element('showDivide').write("/")
    numbers.append("/")

def opTimes():
    Element('showTimes').write("*")
    numbers.append("*")

def opMod():
    Element('showMod').write("%")
    numbers.append("%")


def showNumbers():
    num = ''.join(numbers)
    calcLogic(num)
    # numDisplay = ' '.join(numbers)
    # regexNum = re.split('\+|-|%|/|\*|', num)
    # numDisplay = ' '.join(regexNum)
    numDisplay = re.sub("(\+|-|%|/|\*|)", "(\+|-|%|/|\*| )", num)
    mainCalcBox = Element("mainCalcDisplay")
    mainCalcBox.write(numDisplay)


def calcIn():
    input_box = Element("calc_input")
    calcOut = input_box.value
    mainCalcBox = Element("calcBox")
    mainCalcBox.write(calcOut)

