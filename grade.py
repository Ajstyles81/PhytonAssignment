first_grade = int(input("Enter first grade: "))
second_grade = int(input("Enter second grade: "))
third_grade = int(input("Enter third grade: "))

Average = first_grade + second_grade + third_grade
Sum = Average//3

if first_grade >= 90: grade1 = 'A'
elif first_grade >= 80: grade1 = 'B'
elif first_grade >= 70: grade1 = 'C'
elif first_grade >= 60: grade1 = 'D'
elif first_grade >= 0: grade1 = 'f'

if first_grade >= 90: grade2 = 'A'
elif second_grade >= 80: grade2 = 'B'
elif second_grade >= 70: grade2 = 'C'
elif second_grade >= 60: grade2 = 'D'
elif second_grade >= 0: grade2 = 'f'

if first_grade >= 90: grade3 = 'A'
elif second_grade >= 80: grade3 = 'B'
elif second_grade >= 70: grade3 = 'C'
elif second_grade >= 60: grade3 = 'D'
elif second_grade >= 0: grade3 = 'f'



print(grade1)
print(grade2)
print(grade3)
print ("The total Average of Score inputed is:" , Sum)