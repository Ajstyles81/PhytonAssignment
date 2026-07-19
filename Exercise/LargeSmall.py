NumberOne = int(input("Enter first Integer: "))
NumberTwo = int(input("Enter Second Integer: "))
NumberThree = int(input("Enter Third Integer: "))

Largest = NumberOne
Smallest = NumberOne

Sum = NumberOne + NumberTwo + NumberThree
Average = (NumberOne + NumberTwo + NumberThree)//3
Product = NumberOne * NumberTwo * NumberThree

if Largest > NumberTwo and Largest > NumberThree: print(Largest, "is the Largest")
if NumberThree > Largest: print(NumberThree, " is the Largest")

if Smallest < NumberTwo and Smallest < NumberThree: print(Smallest, "is the Smallest")
if NumberTwo < Smallest: print(NumberTwo, " is the Smallest")
