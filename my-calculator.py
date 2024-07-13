"""
function power, but better ??
"""
def pow2(a,b):
    return a *b

"""
substract two  numbers
"""
def sub(a,b):
    return a - b




"""
Divide two number, the second one must be different than 0 otherwise it will failed
"""
def realDiv(a,b):
    if b != 0:
        return a/b
    else :
        raise ValueError("the second number cannot be negative")



"""
Add two numbers together and return result.
"""

def sum(a, b):
    return a + b



"""
Main function for the calculator app. It provides and interface for the function sum, realDiv, sub & Pow
Loop indefinitly until CTRL + C is enter or the quit button is pressed.
"""
def main():
    while True:
        print("Select operation :")
        print("1. Addition")
        print("2. Subtraction")
        
        print("3. Power")
        print("4. Division")
        print("5. Quit (or CTRL + C)")

        choice = input("Enter choice : ")

        if choice == "1":
            try :
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                returnNumber = sum(number1,number2)
                print("result is : ")
                print(f"{returnNumber}")
            except ValueError :
                print("please enter a valid number (float)")
            #print(f"Result: {sum(num1, num2)}")
        if choice == "2":
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            returnNumber = sub(number1,number2)
            print("result is : ")
            print(f"{returnNumber}")
        
        if choice == "3":
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            returnNumber = pow2(number1,number2)
            print("result is : ")
            print(f"{returnNumber}")

        if choice == "4":
            try : 
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                returnNumber = realDiv(number1,number2)
                print("result is : ")
                print(f"{returnNumber}")
            except ValueError: 
                print("please enter a number different than 0 for the second number")
        if choice == "5" :
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

