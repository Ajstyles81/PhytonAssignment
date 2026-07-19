# user input age 
# use if statement to calculate the ticket price
# if age lesser than five then print free

age = int(input("Enter your age: "))

if age < 5: print("Ticket is free")
elif age >= 5 and age <= 12: print("Your ticket price is 5$")
elif age >= 13 and age <= 64: print("Your ticket price is 12$")
elif age >= 65: print("Your ticket price is: 8$")
