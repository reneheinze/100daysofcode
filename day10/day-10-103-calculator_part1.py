
#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

# This dictionary is act as the means in which we call these functions
operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide
}

#assign the value to variable functions
#function = operations["+"]
#call the above function with the variable
#function(2,3)


# Input the first Number 
num1 = int(input("Whats the first Numer?:"))

# Ask for the symbol / operation
operation_symbol = input("Pick an operation :")

# Input the second Number 
num2 = int(input("Whats the second Number?:"))

#Call the function depending on your input and get the result
#operation_result = operations[operation_symbol](num1,num2)

#This is the longer way. Works as well.
calculation_function = operations[operation_symbol]
first_operation_result = calculation_function(num1,num2)

#Output the result in an Fstring.
print(f"{num1} {operation_symbol} {num2} = {first_operation_result}")

# Ask for another  operation
operation_symbol = input("Pick another operation :")
num3 = int(input("Whats the next Number?:"))
print(operation_symbol)
# Instead of using first_operation_result I just call the function.
#calculation_function = operations[operation_symbol]
second_operation_result = calculation_function(first_operation_result,num3)


# I do now have the first operation_result any more. Therefore i´m just calling the function
print(f"{first_operation_result} {operation_symbol} {num3} = {second_operation_result}")
