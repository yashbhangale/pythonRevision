# Program make a simple calculator

# This function adds two numbers
def add(x, y):    # def keyword is used to define a function,
    return x + y  # A return statement is used to end the execution of the function call and “returns” the result

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:  # while loop we can execute a set of statements as long as a condition is true.
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ") #The choice() method returns a randomly selected element from the specified sequence.

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1': #If condition is evaluated to True , the code inside the body of if is executed. If condition is evaluated to False , the code inside the body of if is skipped.
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3': # elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")