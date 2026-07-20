inputAlpha = (input("Enter Word: "))

if len(inputAlpha) < 5: print("Short String")
if len(inputAlpha) > 5 or len(inputAlpha) == 10: print("Medium String")
if len(inputAlpha) > 10: print("Long String")