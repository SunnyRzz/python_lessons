budget = float(input("Please enter your budget: "))
milkshakes = {1: ("Chocolate",2.00), 2: ("Vanilla",3.00), 3: ("Banana",4.00), 4: ("Strawberry",5.00)}


print("""Milkshake Menu!: 
\n 1.	Chocolate
\n 2.	Vanilla
\n 4.	Strawberry
""")

for flavour, price in milkshakes.items():
    print(f"{flavour} costs {price}")

choise=1


