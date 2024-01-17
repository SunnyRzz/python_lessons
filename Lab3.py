# #Task 1 Squares using while
# x= 1
# while x in range(1,101):
#     print(x, " squared = ", x**2)
#     x+=1
#     if x**2 > 2000:
#         break


## using for

# for x in range(1,101):
#     y = x**2
#     if y >2000:
#         break
#     print(x, " squared = ", y)

# #Task 2 Factorial using while
# integervalue = int(input("Please input an integer: "))    
# factorial = 1
# while integervalue > 1:
#     factorial *= integervalue 
#     integervalue -= 1
# print("factorial: ", factorial)

##using for

# integervalue = int(input("Please input an integer: "))    
# factorial = 1
# for i in range(1,integervalue+1):
#     factorial *= i
# print("factorial: ", factorial)


# #Task 3 Investment
# initial_investment=float(input("Please enter your initial investment £"))
# target_value= float(input("Please enter your target value £"))
# interest_rate= int(input("Please enter your Annual interest rate %"))
# interest_rate_calculated= 1 +(interest_rate/100)
# counter=0
# current_value= initial_investment

# while current_value <= target_value:
#     current_value *= interest_rate_calculated
#     counter += 1
# print(f"It will take you {counter} years to reach the target value of £{target_value} with an initial investment of £{initial_investment} at an annual interest rate of {interest_rate}%")


# #Task 4 
# min=1
# max=100
# uservalue=0
# counter2=0
# while uservalue < min or uservalue > max:
#     uservalue = int(input(f"Please enter a valid value between {min} and {max} "))
#     counter2 +=1
#     if counter2 == 3:
#         print(None)
#         break
# else:
#     print(uservalue)

# Chris's way:
# min_value = 1
# max_value = 100
# attempts = 0

# while attempts < 3:
#     value = int(input(f"enter an integer between {min_value} and {max_value}: "))

#     if min_value <= value <= max_value:
#         print(f"valid integer entered: {value}")
#         break
#     else:
#         print("invalid integer - try again!")
#     attempts += 1
# if attempts == 3:
#     print("None")
    

# #Task 5 (3) Count Vowels when
# word = (input("Please enter a word: ")).lower()
# num_of_vowels=0
# characters = len(word)
# counter3 = 0
# while counter3 < characters:
#     x = word[counter3]
#     if  x in ("a","e","i","o","u"):
#         num_of_vowels += 1
#     counter3 += 1
# print(f"There are {num_of_vowels} vowels in the word {word}")

# #Lab 4 part 2 Task 1 (3) Count Vowels for
word = (input("Please enter a word: ")).lower()
num_of_vowels=0
for i in word:
    if  i in ("a","e","i","o","u"):
        num_of_vowels += 1
print(f"There are {num_of_vowels} vowels in the word {word}")


# # Task 6 (5) Exam Average
# maths_mark = 999 
# english_mark = 999
# ict_mark = 999

# while (maths_mark < 0 or maths_mark > 100):
#     maths_mark = int(input("Enter maths mark(0-100): "))
# while (english_mark < 0 or english_mark > 100):
#     english_mark = int(input("Enter english mark(0-100): "))
# while (ict_mark < 0 or ict_mark > 100):
#     ict_mark = int(input("Enter ict mark(0-100): "))

# average_mark = (maths_mark + english_mark + ict_mark) / 3

# if average_mark >= 65:
#     result = "pass"
# else:
#     result = "fail"

# print(f"average mark: {average_mark}: {result}")

