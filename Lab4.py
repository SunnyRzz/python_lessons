#part 1
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
num_ages = len(ages)
# print(num_ages)

# for age in ages:
#     print(age)

# for age1 in ages:
#     x= age1+1
#     print(x)
for i in range(len(ages)):
    ages[i] +=1 
print(ages)
# for age2 in ages:
#     if age2 < 16 or age2 > 65:
#         del(age2)
#     else:
#         print(age2)

specific_age=[]
for age2 in ages:
    if age2 >= 16 and age2 <= 25:
        specific_age.append(age2)
    else:
        continue
print(specific_age)
print(len(specific_age))

ages.sort()
for age in ages:
    print(age)

# proportion

count = 0
for age in ages:
    if age >= 16 and age <= 25:
        count += 1
proportion = count / len(ages)
print(proportion)

# # #Lab 4 part 2 Task 1 (3) Count  
# word = (input("Please enter a word: ")).lower()
# num_of_vowels=0
# for i in word:
#     if  i in ("a","e","i","o","u"):
#         num_of_vowels += 1
# print(f"There are {num_of_vowels} vowels in the word {word}")