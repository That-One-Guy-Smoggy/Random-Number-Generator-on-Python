import random
import time 

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

## We take the inputs from the use, in this case first and second number.
firstNumber = float(input("""
*********************************************
********** Random Number Generator **********
***************** By Smoggy *****************
*********************************************
 
Please input an integer: """))

secondNumber = float(input("Please input a higher integer: "))

## This saves the result from the functions on a var
firstNumber = int(roundNumber())
secondNumber = int(roundNumber2())

## Saves the genrated number within a variable
generatedNumber = random.randrange(firstNumber, secondNumber)

## Prints the result 
#The time.sleep command indicates the time between
time.sleep(1.5)
print("The generated number has been selected!!!")
time.sleep(1)
print("____________________________________________")
print("Your new number is: ", generatedNumber)

#The following  repeats the program once more
##
repeat = input("Would you like to generate another number? (Y/N): ")
while repeat == "Y":
    firstNumber = (input("Please input a number: "))
    secondNumber = (input("Please input a higher number: "))
    print(firstNumber,secondNumber)
    generatedNumber = random.randrange(firstNumber, secondNumber)
    time.sleep(1.5)
    print("The generated number has been selected!!!")
    time.sleep(1)
    print("____________________________________________")
    print("Your new number is: ", generatedNumber)
    repeat = (input("Would you like to generate another number? (Y/N): "))
else:
    print("Press any key to exit")
    

    

## Made Fully By Smoggy
## GitHub --- @That-One-Guy-Smoggy
## Twitter --- @Smoggy445
