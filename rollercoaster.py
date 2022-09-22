print("Welcome to the rollercoaster! ")

height = int(input("What is your heat in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5 ")
    elif age <= 18:
        bill =7
        print("Youth tickets are $7. ")
    else:
        bill = 12
        print("Adult tickets are $12 ")
    #Make sure the else is at the same indent level as the if

    wants_photo = input("Do you want a photo taken? Y or N")
    if wants_photo == "Y":
        #Add three dollars to the bill
        bill += 3
        print(f"Your final bill {bill}")


else:
    print("Sorry :(. You are too short to ride the roller coaster.")