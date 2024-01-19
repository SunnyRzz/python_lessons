# import csv

# companies = []
# sales = []

# with open('/home/sunny/git/python_lessons/files/fileLab.py', newline='') as csvfile:
#     reader = csv.reader(csvfile) 
#     for row in reader:
#         print(row)


import csv

companies = []
sales = []

with open('/home/sunny/git/python_lessons/files/fileLab.py', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        # If you want to separate columns into different lists, you can do it here.
        # For example, assuming the first column is company name and the second is sales:
        # companies.append(row[0])
        # sales.append(row[1])

