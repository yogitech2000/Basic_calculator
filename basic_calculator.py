def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
    
def loop(): #This is help to looop the function when we call back
    print("chooose the option which you want to do:\n[1]addition\n[2]subtraction\n[3]multiplication\n[4]divition")
    n = input("choose option: ")
    l = ["1","2","3","4"] #This is for check the input whether the option is exist or not.
    
    if n in l:
        if n=="1": # This is for Addition
            a = int(input("number1: "))
            b = int(input("number2: "))
            print(add(a,b))
        
        if n=="2": #This is for Subtraction
            a = int(input("number1: "))
            b = int(input("number2: "))
            print(sub(a,b))
            
        if n=="3":#This is for Multiplication
            a = int(input("number1: "))
            b = int(input("number2: "))
            print(mul(a,b))
            
        if n=="4": #This is for Division
            a = int(input("number1: "))
            b = int(input("number2: "))
            print(div(a,b))
    else: 
        print("\n\nSorry! invalid input. Please try again!")
        
    
loop() #This is for calling the function at the begining.
def Value():
    N = input("Do you want to try another sum? Y/N: ")
    if N == "Y" or N == "y" or N=="Yes" or N == "yes":
        print("\n\n")
        loop() #This is for call back if we need to try once again to calculate the maths.
        return Value()
    else:
        print("The code was end!\nThanks to use me!\nRun it again \U0001f609")
        
Value() 
