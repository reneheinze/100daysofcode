# Write your code below this line 👇

year = (int(input("Which year do you want do check? ")))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")

    else:
        print("Leap year.")    

else:
    print("Not leap year.")

#You can turn any sort of logic into a flowchart to be able to visualize it.
#Once you got your logic straight, converting it into code is much much simpler.


