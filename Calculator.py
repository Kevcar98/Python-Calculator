import time
import math
import operator
import functools



def Plus():
    variables= {} #Makes dictionary
    num = 1 
    try:
        usertimes=int(input("How many times? ")) # How many variable you want there to be
        Valid = True
        pass
    except ValueError:
        print("That was not a valid number.  Try again...")
        Valid=False
        while Valid == False:
            try:
                usertimes=int(input("How many times? "))
                Valid = True
                pass
            except ValueError:
                print("That was not a valid number.  Try again...")
                Valid=False
                # How many variable you want there to be
                
    print()
    try:
        variables[num]=int(input("Enter first number: ")) # How many variable you want there to be
        Valid = True
        pass
    except ValueError:
        print("That was not a valid number.  Try again...")
        Valid=False
        while Valid == False:
            try:
                variables[num]=int(input("Enter first number: "))
                Valid = True
                pass
            except ValueError:
                print("That was not a valid number.  Try again...")
                Valid=False

    while num != usertimes:
        num += 1
        try:
            variables[num]=int(input("Enter next number: ")) # How many variable you want there to be
            Valid = True
            pass
        except ValueError:
            print("That was not a valid number.  Try again...")
            Valid=False
            while Valid == False:
                try:
                    variables[num]=int(input("Enter next number: "))
                    Valid = True
                    pass
                except ValueError:
                    print("That was not a valid number.  Try again...")
                    Valid=False


    print("Your answer is", sum(variables.values()))
    print()
    print()
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()



def Minus():

    
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    ans = num1-num2
    print()    
    print()
    print("Your answer is", ans)
    print()
    print()
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()


def Multiply():

    variables= {} #Makes dictionary
    num = 1 
    try:
        usertimes=int(input("How many times? ")) # How many variable you want there to be
        Valid = True
        pass
    except ValueError:
        print("That was not a valid number.  Try again...")
        Valid=False
        while Valid == False:
            try:
                usertimes=int(input("How many times? "))
                Valid = True
                pass
            except ValueError:
                print("That was not a valid number.  Try again...")
                Valid=False
    print()
    try:
        variables[num]=int(input("Enter first number: ")) # How many variable you want there to be
        Valid = True
        pass
    except ValueError:
        print("That was not a valid number.  Try again...")
        Valid=False
        while Valid == False:
            try:
                variables[num]=int(input("Enter first number: "))
                Valid = True
                pass
            except ValueError:
                print("That was not a valid number.  Try again...")
                Valid=False
                
    while num != usertimes:
        num += 1
        try:
            variables[num]=int(input("Enter next number: ")) # How many variable you want there to be
            Valid = True
            pass
        except ValueError:
            print("That was not a valid number.  Try again...")
            Valid=False
            while Valid == False:
                try:
                    variables[num]=int(input("Enter next number: "))
                    Valid = True
                    pass
                except ValueError:
                    print("That was not a valid number.  Try again...")
                    Valid=False

    #sets the next variable to dictionary               
    list1=variables.values()
    ans=functools.reduce(operator.mul, list1, 1)

    print()    
    print()
    print("Your answer is", ans)
    print()
    print()
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()


def Divide():
    num1 = float(input("Enter the first Number: "))
    num2 = float(input("Enter the second Number: "))
    ans = num1 / num2
    print()
    print()
    print("Your answer is", ans)
    print()
    print()
    out = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()



def Square():
    num=float(input("Please type in what number you want to square: "))
    ans = num* num
    print()
    print()
    print("Your answer is",ans)
    exits = str(input("Do you want to exit the program Y/N: "))

      
    
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()
    

def SQR():
    num=float(input("Please type in what number you want to Square Root: "))
    ans = math.sqrt(num)
    print()
    print()
    print("Your answer is",ans)
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()


def Cos():
    num=float(input("Please type in what number you want to use Cosine on: "))
    ans = math.cos(num)
    print()
    print()
    print("Your answer is",ans, "in radians.")
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()

def Sin():
    num=float(input("Please type in what number you want to use Sin on: "))
    ans = math.sin(num)
    print()
    print()
    print("Your answer is",ans, "in radians.")
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()

def Tan():
    num=float(input("Please type in what number you want to use Tan on: "))
    ans = math.tan(num)
    print()
    print()
    print("Your answer is",ans, "in radians.")
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()

def NLog():
    num=float(input("Please type in what number you want to use the natural log on: "))
    ans = math.log(num)
    print()
    print()
    print("Your answer is",ans,".")
    exits = str(input("Do you want to exit the program Y/N: "))
    if exits == "Y" or exits == "y" or exits == "yes" or exits == "Yes":
        exit()
    else:
        print()
    print()
    print()
    print()
    print()
    print()
    time.sleep(2)
    mainmenu()
    



def mainmenu():

    
    print("                   _______________")
    print("                  /__/_______\____\\")
    print("                 /__/          \___\\")
    print("                /__/            \___\\")
    print("               |___| CALCULATOR |____|")
    print("                \___\ Main Menu /___/")  
    print(" _______________ \___\_________/___/_______________")
    print("/________________ \_______________/________________\\")
    print("| __     __                      ______        __   |")
    print("|/  |   /  |                    /      \     _/  |  |")
    print("|$$ |   $$ | ______    ______  /$$$$$$  |   / $$ |  |")
    print("|$$ |   $$ |/      \  /      \ $$$  \$$ |   $$$$ |  |")
    print("|$$  \ /$$//$$$$$$  |/$$$$$$  |$$$$  $$ |     $$ |  |")
    print("| $$  /$$/ $$    $$ |$$ |  $$/ $$ $$ $$ |     $$ |  |")
    print("|  $$ $$/  $$$$$$$$/ $$ | __   $$ \$$$$ |__  _$$ |_ |")
    print("|   $$$/   $$       |$$ |/  |  $$   $$$//  |/ $$   ||")
    print("|    $/     $$$$$$$/ $$/ $$/    $$$$$$/ $$/ $$$$$$/ |")
    print("| __________________________________________________|")
    print(" \_________________________________________________/")     
    
    print("""
              _____________________
             |  _________________  |
             | | Made by: Kevin  | |
             | |    ENJOY! ;D    | |
             | |   0123456789    | |
             | |_________________| |             
             |  __ __ __ __ __ __  |
             | |__|__|__|__|__|__| |
             | |__|__|__|__|__|__| |
             | |__|__|__|__|__|__| |
             | |__|__|__|__|__|__| |
             | |__|__|__|__|__|__| |
             | |__|__|__|__|__|__| |
             |  ___ ___ ___   ___  |
             | | 7 | 8 | 9 | | + | |
             | |___|___|___| |___| |
             | | 4 | 5 | 6 | | - | |
             | |___|___|___| |___| |
             | | 1 | 2 | 3 | | x | |
             | |___|___|___| |___| |
             | | . | 0 | = | | / | |
             | |___|___|___| |___| |
             |_____________________|



                                                                                   """)
    main()
        

def main():
    print()
    Symbol= input("Do you want to Add/Subtract/Multiply/Divide/\n             Square/Square Root/Cosine/Sin/Tan/Natural Log: ")
    print()
    
   
    if Symbol == "Add" or Symbol == "add" or Symbol == "+":
        Plus()

    elif Symbol == "Subtract" or Symbol == "subtract" or Symbol == "-":
        Minus()

    elif Symbol == "Multiply" or Symbol == "multiply" or Symbol == "*" or Symbol == "x" or Symbol == "X":
        Multiply()

    elif Symbol == "Divide" or Symbol == "divide" or Symbol == "/":
        Divide()


    elif Symbol == "Square" or Symbol == "square" or Symbol == "^2" or Symbol == "2":
        Square()

    elif Symbol == "Square Root" or Symbol == "square root" or Symbol == "Square root" or Symbol == "SQR" or Symbol == "Sqr" or Symbol == "sqr":
        SQR()

    elif Symbol == "COS" or Symbol == "Cos" or Symbol == "cos" or Symbol == "C" or Symbol == "c" or Symbol == "cosine" or Symbol == "Cosine":
        Cos()
        
    elif Symbol == "Sin" or Symbol == "sin":
        Sin()
        
    elif Symbol == "Tan" or Symbol == "tan":
        Tan()

    elif Symbol == "NLOG" or Symbol == "NLog" or Symbol == "Nlog" or Symbol == "nlog" or Symbol == "NL" or Symbol == "Nl" or Symbol == "nl" or Symbol == "Natural Log" or Symbol == "natural log":
        NLog()
    
    else:
        print("Option not available, please try again.")
        main()







    




mainmenu()






