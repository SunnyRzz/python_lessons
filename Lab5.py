import statistics
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades=[]
grades=data.split(",")
#grades = list(map(int, grades))
grades = [int(grade) for grade in grades]

print(grades)

lowest_grade = min(grades)
print(f"The lowest grade is: {lowest_grade}")
highest_grade = max(grades)
print(f"The highest grade is: {highest_grade}")

y=0
for x in grades:
    y += x
z = y / len(grades)
print(f"The average of the grades are {z}")

b=0
b=sum(grades)
print(f"The sum of the grades are {b}")
c= y / len(grades)
print(f"The average of the grades are {round(c,2)}")

d= statistics.mean(grades)
print(f"The mean of the grades are {round(d,2)}")

e= statistics.median(grades)
print(f"The median of the grades are {round(e,2)}")

print(f"From the inputted grades, the min grade is {lowest_grade}, the max grade is {highest_grade}, the average is {round(c,2)}, the mean is {round(d,2)}, and the median is {round(e,2)}")
