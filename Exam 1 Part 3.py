#Exam 1 part 3
#Question 1 & 2
print("Question 1&2 Results")
numbs = [3, 6, 8, 12, 5, 9, 10]
print("The evens are:")
for num in numbs:
    if num%2 == 0:
        print(num)
        
print("")
#Question 3
def myMean(myInput):
    mySum = 0.0
    for inp in myInput:
        mySum = mySum+inp
    theMean = mySum/float(len(myInput))
    return(theMean)


def myMax(myInput):
    theMax = -999999
    for currentNum in myInput:
            if currentNum > theMax:
                theMax = currentNum
    return(theMax)


def myMin(myInput):
    theMin = 99999
    for currentNum in myInput:
        if currentNum < theMin:
            theMin = currentNum
    return(theMin)


def myRange(myInput):
    theMax = myMax(myInput)
    theMin = myMin(myInput)
    theRange = theMax - theMin
    return theRange

import math
def myStd(myInput):
    theMean = myMean(myInput)
    sumSquares = 0
    theVariances = []
    squaredVariances = []
    for currentNum in myInput:
        theVariances.append(currentNum - theMean)
    for currentNum in theVariances:
        squaredVariances.append(currentNum * currentNum)
    for currentNum in squaredVariances:
        sumSquares = currentNum + sumSquares
    finalVariance = sumSquares/6
    return(math.sqrt(finalVariance))
print("Question 3 Results")
print("The mean is "+ str(round(myMean(numbs),2)))
print("The Max is "+ str(myMax(numbs)))
print("The Range is "+str(myRange(numbs)))
print("The Standard Deviation is "+str(round(myStd(numbs),3)))
print("")

# question 4
print("Question 4 Results")
import StatCalculator
numbs = list(range(1,1001))
print("The average of 1-1000 is "+str((StatCalculator.myMean(numbs))))
print("The standard Deviation of 1 - 1000 is "+str(round((StatCalculator.myStd(numbs)),2)))
