#Make a tip calculator that makes the tip for the bill

#Welcome to the tip calculator
print("Welcome to the Tip Calculator!")

#Ask for total bill
bill = float(input("what was the total bill? $"))

#What percentage tip would you like to give?
tip = int(input("Please select a tip percentage: 10 , 12, or 15? Or Enter your own amount:"))

#How many people split teh bill
people = int(input("How many people ate with you? "))

bill_with_tip = tip / 100 * bill + bill / people

final = f"The amount each person pays is {bill_with_tip}"

print(final)
