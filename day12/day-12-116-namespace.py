################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# local Scope
# If I create a variable inside a function, it is only accessible in that function. 
# That variable has local scope to that function.

#def drink_potion():
#    potion_strength = 2
#    print(potion_strength)

#drink_potion()
#print(potion_strength)

# Global Scope
# If I want to make the variable available everywhere I have to define it in a global scope.

# Namespace
# Anything that I give a name to has a namespace. And that Namespace  is valid in certain scopes. 

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
