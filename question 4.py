# section א
import math

num1 = input("enter a number: ")
num2 = input("enter a second number: ")
print(num1 == num2)


# section ב
num3 = input("enter a number: ")
num4 = input("enter a second number: ")
sum = int(num3) + int(num4)
print(sum == 8)

# section ג
NUM5 = 55
NUM6 = 46
SUM = NUM5 + NUM6
print(SUM)

# section ד
num7 = 45
num8 = 81
temp = num7
num7 = num8
num8 = temp
# or
num7, num8 = num8, num7

# section ה
height = int(input("please enter a height: "))
base = int(input("please enter a base: "))
print("the surface of the triangle is: ", height * base)

# section ו
num9 = float(input("please enter a number: "))
print(num9 % 2 != 0)

# section ז
num10 = float(input("please enter a number: "))
print(num10 ** 0.5)

# section ח
grade1 = int(input("please enter a grade: "))
grade2 = int(input("please enter a second grade: "))
grade3 = int(input("please enter a third grade: "))
print("the average is: ", (grade1 + grade2 + grade3)/3)

# section ט
kilometers_num = float(input("please enter num of kilometers: "))
print(kilometers_num, "kilometers are ", kilometers_num * 0.62, " miles")



