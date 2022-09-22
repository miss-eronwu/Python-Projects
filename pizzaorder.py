print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you want? S, M, or L ")
if size == "S":
    bill = 15
    print("You picked a small pizza")
elif size == "M":
    bill = 20
    print ("You picked a medium pizza")
else:
    bill = 25
    print("You picked a large pizza")

add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y":
        bill += (2 + "S")
        bill += (3 + "M")
        bill+= (3 + "L")
        print("You've added pepperoni to your pizza :)")

else:
        print("You've decided no pepperoni")

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
        bill += 1
        print("you've added extra cheese")

else:
        print("You've decided on no cheese")

final_bill = print("Your final bill is: " + str(bill))

print(final_bill)
