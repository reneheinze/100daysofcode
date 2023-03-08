# global

enemies = 1

def increase_enemies():
# global takes the global enemies into the function and allows to modify it.
# Without global i only have read access to enemies.
  global enemies
  enemies +=1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# a better approach would be not to modify the global variable
def increase_enemies():
  return enemies + 1

