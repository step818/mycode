#!/usr/bin/env python3

def calculator():
    try:
        x = float(input("Enter in a number: "))
        y= float(input("Enter ANOTHER  number: "))
    except:
        print("Invalid input, try again.")
        calculator()

    operation = ""
    while(operation != "add" and operation != "subtract" and operation != "divide" and operation != "multiply"): 
        
    
     operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()
    if(operation == "add"):
        add(x, y)
    elif(operation == "subtract"):
        subtract(x, y)
    elif(operation == "divide"):
        divide(x, y)
    elif(operation == "multiply"):
        multiply(x, y)
    else:
        print("use a valid OPTION")
        #continue
     


def add(x, y):
    answer = x + y
    print(answer)

def subtract(x, y):
    answer = x - y
    print(answer)

def divide(x, y):
    answer = x / y
    print(answer)

def multiply(x, y):
    answer = x * y
    print(answer)

calculator()
