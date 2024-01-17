num = 10
num_1=1

while num > num_1:
    print(num)
    break
else:
    print(num_1)

largest = num *(num> num_1) + num_1 * (num_1 > num)
# 10 * TRUE + 1 * FALSE