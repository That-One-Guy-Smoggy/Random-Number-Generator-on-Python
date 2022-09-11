import random
import time 

## We take the inputs from the use, in this case first and second number.
firstNumber = float(input("""
*********************************************
********** Random Number Generator **********
***************** By Smoggy *****************
*********************************************
 
 Please input an integer: """))

secondNumber = float(input("Please input a higher integer: "))

## The followent functions round the number given incase it's a float 
def roundNumber():
    if firstNumber == float:
        return round(firstNumber)
    else:
        return firstNumber

def roundNumber2():
    if secondNumber == float:
        return round(secondNumber)
    else:
        return secondNumber

## This saves the result from the functions on a var
firstNumber = int(roundNumber())
secondNumber = int(roundNumber2())

## Saves the genrated number within a variable
generatedNumber = random.randrange(firstNumber, secondNumber)

## Prints the result 
time.sleep(2) #The time.sleep command indicates the time between 
print("The generated number has been selected!!!")
time.sleep(1)
print(" ____________________________________________")
print("Your new number is:", generatedNumber)


#Made Fully By Smoggy --- That-One-Guy-Smoggy
