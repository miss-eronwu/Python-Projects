#Build a calculator

calculator = ( '''
|  _________________  |
| | JO  3.141592654 | |
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
'''
)
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
print("Welcome to the calculator" + calculator)
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))


for operate in operations:
    print(operate)

operation_symbol = input("Pick an symbol from the line above: ")

if operation_symbol == "+":
   answer = add(num1, num2)
   print(f"{num1} {operation_symbol} {num2} = {answer}")
elif operation_symbol == "-":
    subtract(num1, num2)
    answer = subtract(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
elif operation_symbol == "*":
    answer = multiply(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
elif operation_symbol == "/":
    answer = divide(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
else:
     print("That's not a valid entry")

