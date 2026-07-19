first_grade = int(input("Enter first grade: "))
second_grade = int(input("Enter second grade: "))
third_grade = int(input("Enter third grade: "))

Average = first_grade + second_grade + third_grade
Sum = Average//3

if first_grade >= 90: grade1 = 'A'
elif first_grade >= 80: grade1 = 'B'
elif first_grade >= 70: grade1 = 'C'
elif first_grade >= 60: grade1 = 'D'
else: grade1 = 'F'

if second_grade >= 90: grade2 = 'A'
elif second_grade >= 80: grade2 = 'B'
elif second_grade >= 70: grade2 = 'C'
elif second_grade >= 60: grade2 = 'D'
else: grade2 = 'F'

if third_grade >= 90: grade3 = 'A'
elif third_grade >= 80: grade3 = 'B'
elif third_grade >= 70: grade3 = 'C'
elif third_grade >= 60: grade3 = 'D'
else: grade3 = 'F'


print()
print("First grade Entered" ,grade1)
print("Second grade Entered" ,grade2)
print("Third grade Entered" ,grade3)
print ("The total Average of Score inputed is:" , Sum)