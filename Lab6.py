# Task income tax

def getincometax(salary):
    tax_value=0
    if salary <= 11850:
        tax_value += 0
    elif salary <= 34500:
        tax_value += ((salary-11850)*0.20)
    elif salary <= 150000:
        tax_value += (((34500-11850)*0.20) + ((salary - 34500)*0.40))
    elif salary > 150000:
        tax_value += (((34500-11850)*0.20) + ((150000-34500)*0.40) + ((salary-150000)*0.45))
    else:
        print("You have entered a invalid salary")
    print(f"With a salary of £{salary} you will pay £{tax_value} in tax")

getincometax(150000)