# Part1
#if
age = int(input("Please enter your age: "))

if age >= 18:
    print('You are in category A')
if age >= 16:
    print('You are in category B')
if age < 16:
    print('You are in category C')

# #elif
age = int(input("Please enter your age: "))

if age >= 18:
    print('You are in category A')
elif age >= 16:
    print('You are in category B')
else:
    print('You are in category C')

#Part2
#Calculator
    
number1=float(input("Please enter the first value: "))
number2=float(input("Please enter the second value: "))

print("""Available operations: 
\n 1.	Add      +
\n 2.	Subtract - 
\n 3.	Multiply * 
\n 4.	Divide   / 
\n 5.	Square(to the power of)   s
""")

operation = input("Please enter the sign from above for the operation required: ")

while operation not in ("+","-","*","/","s"):
    print(f"Sorry the operation {operation} is not recognised, please enter an operation from above")
    operation = input("Please re-enter the sign from above for the operation required: ")
else:
    if operation == "s":
        print(number1, "to the power of", number2, "= ", number1**number2)
    elif operation == "*":
        print(number1, "Multiplied by", number2, "= ", number1*number2)
    elif operation == "/":
        print(number1, "Divided by", number2, "= ", number1/number2)
    elif operation == "+":
        print(number1, "Add", number2, "= ", number1+number2)
    elif operation == "-":
        print(number1, "Subtract", number2, "= ", number1-number2)

#Task2
        
mark = int(input("Please enter your mark between 1 and 100: "))
while mark > 100 or mark < 1:
    print(f"Sorry the mark you entered - {mark} - is not in the range of 1 to 100, please re-enter")
    mark = int(input("Please re-enter your mark between 1 and 100: "))
else:
    if mark >= 71:
        print("You have been graded with a Distinction")
    elif mark >= 61:
        print("You have been graded a Merit")
    elif mark >= 50:
        print("You have been graded a Pass")
    else:
        print("You have failed ")

# Task 3

result = int(input("Please enter your mark between 1 and 100: "))
level = int(input("Please input your level: "))

if result > 100 or result < 1:
    print(f"Sorry the mark you entered - {result} - is not in the range of 1 to 100, please re-enter")
elif level == 1:
    if result >= 71:
        print("You have been graded with a Distinction")
    elif result >= 61:
        print("You have been graded a Merit")
    elif result >= 50:
        print("You have been graded a Pass")
    else:
        print("You have failed ")
elif level == 2:
    if result >= 66:
        print("You have been graded with a Distinction")
    elif result >= 51:
        print("You have been graded a Merit")
    elif result >= 40:
        print("You have been graded a Pass")
    else:
        print("You have failed ")
else:
    print(f"Sorry the Level you entered - {level} - is not in the range of 1 or 2, please re-enter")

  