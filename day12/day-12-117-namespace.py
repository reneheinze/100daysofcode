# There is no Block Scope in Pyton

# This variable does have the same scope as its enclosing function.

#if 3 > 2:
#  a_variable = 10

# Example new_enemy is still on the global scope

game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)


# Example new_enemy1 is in local scope to the function.       

game_level = 3
def create_enemy():
  enemies1 = ["Skeleton","Zombie","Alien"]
  if game_level < 5:
    new_enemy1 = enemies1[0]

print(new_enemy1) 

# If i create a variable within a function. Then it is only available within that function. 
# That does not apply to If blocks or a While loop.
# enemies 1 und enemies are two different variables.