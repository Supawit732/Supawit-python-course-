# Complete this program to classify people by age
# age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
print("=" * 40)
print("\tClassify program")
print("=" * 40)

age = int(input("Enter age: "))
if 0 <= age <= 12:
    print(" You is Child")
elif 13 <= age <= 19:
    print("You is Teenager ")
elif 20 <= age <= 59:
    print("You is Adult")
elif 60 <= age <= 150:
    print("You is Senior")
else:
    print("Invaild age")
