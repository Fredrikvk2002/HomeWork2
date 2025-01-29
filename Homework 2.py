# Net salary, given gross salary

from random import choice

# print(f"{choice(drinks)} {choice(mixers)}")
print("I am the virtual tax accountant, welcome to my world")

name = input("How should I call you?")

try:
    GrossSalary = input("What is your gross salary")
    GrossSalary = float(GrossSalary)
    Children = input("How many children do you have?")
    Children = int(Children)


    if GrossSalary < 1000:
        TaxRate = 0.1
    elif GrossSalary < 2000:
        TaxRate = 0.12
    elif GrossSalary < 4000:
        TaxRate = 0.14
    else:
        TaxRate = 0.18

    if GrossSalary < 2000:
        TaxCut = Children * 0.01
    else:
        TaxCut = Children * 0.005

    EffectiveTax = max(0,TaxRate-TaxCut)
    NetSalary = GrossSalary * (1-EffectiveTax)

    print(f"Your net salary is: {NetSalary:.2f}")

except ValueError:
    print("I don't have time for your games. Get out!")