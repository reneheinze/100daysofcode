#Simple Function
def greet():
    print("hi")
    print("good")
    print("looking")

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


#Functions with more that one input
def greet_with_multiple_names(name, location):
    print(f"Hello {name}")
    print(f"How are you doing at {location}")


#calling the function
#greet()
#greet_with_name("Rene")
#greet_with_multiple_names("Rene","Eichwalde")
greet_with_multiple_names(name="Rene",location="Eichwalde")