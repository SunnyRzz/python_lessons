weight = float(input("Please enter your weight as a number (Decimals are accepted): "))
units = input("Please enter whether you weight unit is in Kgs or Lbs: ")

if units not in ("Kgs","Lbs"):
    print(f"Sorry the unit {units} is not recognised, please enter either \"Kgs\" or \"Lbs\"")
elif units == "Kgs":
    converted_kg= (weight * 2.20462262)
    print(f"{weight} {units} equals {converted_kg} Lbs")
elif units == "Lbs":
    converted_lb= (weight / 2.20462262)
    print(f"{weight} {units} equals {converted_lb} Kgs")