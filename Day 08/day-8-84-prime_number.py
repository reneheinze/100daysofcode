# Prime Numbers can only be divided by one and itself
# Is a number that can not be broken in smaller parts other than one and itself
 
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for check in range(2, number):
#        print(f"Check: {check} Number: {number}")
        if check == number:
            print()
        elif number % check == 0:
#            print("Not an Prime")
            is_prime = False
        else:
#            print("Prime")
            print()
#if is_prime is true
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is no prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



