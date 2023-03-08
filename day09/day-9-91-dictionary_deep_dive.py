#define the dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",}

#Retrieving all items from the dictionary 
#print(programming_dictionary)

#Retrieving the item "Bug" from the dictionary 
#print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#print(programming_dictionary)




#Create a empty dictionary
empty_dictionary={}

#Wipe an existing dictionary
#programming_dictionary= {}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"]="A moth in your computer"
#print(programming_dictionary)

#Loop through a dictionary
# When I look throug a dictionary it will loop through the keys.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])