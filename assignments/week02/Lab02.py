"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
print("*" * 40)
print("\t    Currency Converter")
print("*" * 40)
choose = int(input("Do you want to convert THB to USD or USD to THB(if you want thb to usd plese press 1 or thb to usd plese press 2): "))
if choose == 1:
    thb = float(input("Enter Thai Baht: "))
    convertthb = thb / 35.5
    print(f"Amount US Dollars:{convertthb: .2f}")
    print(f"{thb} / 35.5")
elif choose == 2:
    usd = float(input("Enter US Dollars: "))
    convertusd = usd * 35.5
    print(f"Amount Thai Baht:{convertusd: .2f} ")
    print(f"{usd} * 35.5")
else :
    print("Invaid number")
    