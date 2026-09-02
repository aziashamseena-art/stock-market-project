# stock investment tool

print("welcome to the stock investment tool!")

age = int(input("Please enter your age: "))

if age < 18:
    print("Sorry, you must be at least 18 years old to use this tool.")
    exit()
elif age >= 18 and age < 20:
    equity=90;large_cap=50;mid_cap=50;small_cap=25;debt=5;gold=5;
elif age >= 20 and age < 30:
    equity=80;large_cap=50;mid_cap=20;small_cap=10;debt=15;gold=5;
elif age >= 30 and age < 40:
    equity=70;large_cap=45;mid_cap=15;small_cap=10;debt=20;gold=10;
elif age >= 40 and age < 50:
    equity=60;large_cap=40;mid_cap=15;small_cap=15;debt=30;gold=10;
elif age >= 50 and age < 60:
    equity=50;large_cap=35;mid_cap=10;small_cap=5;debt=40;gold=10;
else:
    equity=30;large_cap=25;mid_cap=5;small_cap=0;debt=60;gold=10;

print(f"Based on your age, we recommend the following investment allocation:")
print(f"Equity: {equity}%")
print(f"  Large Cap: {large_cap}%")
print(f"  Mid Cap: {mid_cap}%")
print(f"  Small Cap: {small_cap}%")
print(f"Debt: {debt}%")
print(f"Gold: {gold}%")
