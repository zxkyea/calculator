def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Undefined (A number cannot be divided by 0)"
    return a / b

def calculator():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Please select the operation number (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid number.")
            return
        
        if choice == '1':
            print(f"Result: {addition(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"Result: {division(num1, num2)}")
    else:
        print("Invalid selection!")

calculator()
