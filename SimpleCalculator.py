# Simple Calculator
def calculator():
 num1 = float(input("Enter first number: "))
 operator = input("Enter operator (+, -, *, /): ")
 num2 = float(input("Enter second number: ")) 
 if operator == '+':
    result = num1 + num2
 elif operator == '-':
    result = num1 - num2
 elif operator == '*':
    result = num1 * num2
 elif operator == '/':
    result = num1 / num2
 else:
    result = "Invalid operator"
 print(f"Result: {result}") 
    
calculator()

