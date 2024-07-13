
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
        print("4. Quit (or CTRL + C)")

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
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {sum(num1, num2)}")
        if choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {sum(num1, num2)}")
        if choice == "4":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

