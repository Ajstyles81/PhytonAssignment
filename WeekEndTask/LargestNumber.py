
NumberOne = int(input("Enter First Integer: "))

NumberTwo = int(input("Enter Second Integer: "))

NumberThree = int(input("Enter Third Integer: "))

Largest = NumberOne
if(NumberTwo > Largest): Largest = NumberTwo
if(NumberThree > Largest): Largest = NumberThree
	
	
print("The largest number is: ",Largest)