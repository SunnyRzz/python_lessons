# #Task 1 Squares
# x= 1
# while x in range(1,101):
#     print(x, " squared = ", x**2)
#     x+=1


#Task 2 Factorial
integervalue = int(input("Please input an integer: "))    
factorial = 1
while integervalue > 1:
    factorial *= integervalue 
    integervalue -= 1
print("factorial: ", factorial)