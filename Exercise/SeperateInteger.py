number = int(input("Enter Five-digit integer: "))

numberfive = number % 10
number = number // 10

numberfour = number % 10
number = number // 10

numberthree = number % 10
number = number // 10

numbertwo = number % 10
number = number // 10

numberone = number % 10
print (numberone, numbertwo, numberthree, numberfour, numberfive, sep="  ")