names=[]
while len(names) < 5:
    name = input(f"Please input name {len(names)+1}: " )
    names.append(name)

x = 0
while x < len(names):
    print(names[x], "Is Awesome")
    x += 1

for i in range(len(names)):
    print(names[i], "Is Awesome")

