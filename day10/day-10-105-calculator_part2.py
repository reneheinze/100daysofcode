
#Calculator
from art import logo

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


def calculator():
    print(logo)
    # Variables / Set Tag
    calculating_finished = False
    # Input the first Number 
    num_first = float(input("What's the first Number?:"))
    
    for symbol in operations:
        print(symbol)  

    while not calculating_finished == True:
        # Ask for the symbol / operation
        operation_symbol = input("Pick an operation :")
        # Input the next Number 
        num_next = float(input("Whats the next Number?:"))
        #Call the function depending on your input and get the result
        operation_result = operations[operation_symbol](num_first,num_next)
        #This is the longer way. Works as well.
        #calculation_function = operations[operation_symbol]
        #first_operation_result = calculation_function(num1,num2)

        #Output the result in an Fstring.
        print(f"{num_first} {operation_symbol} {num_next} = {operation_result}")
        ask_quit = input("Type 'y' to continue calculating with, or type 'n' to start a new calculation.: ")
        if ask_quit  != 'y':
            calculating_finished = True
            calculator()
        else:
            num_first = operation_result

calculator()
