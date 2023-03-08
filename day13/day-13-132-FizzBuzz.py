for number in range(1, 101):
  #1.bug = or
  #2.bug if = elif
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  #3. bug Square Brackets
  else:
    print(number)