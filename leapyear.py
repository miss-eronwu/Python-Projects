#Make an interface that tells the user if a year they input is a leap year.

#Leap Year has 366 days in a year, an extra day is added in February
#every year that is divisible by four
#except every year that is divisible by 100
#unless the year is also evenly divisible by 400

print("Welcome to the Leap Year Checker ! ")

leap_year = (int(input("Please insert the year, and the computer will tell you if it's a leap year\n")))


#every year that is divisible by four
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap Year")
else:
    print("not a Leap Year")


#except every year that is divisible by 100



#unless the year is also evenly divisible by 400
