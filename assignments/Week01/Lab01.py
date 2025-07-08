# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
name = input("What is you name: ")
age = int(input("How old are you: "))
email = input("Enter you Email:")
phone = int(input("Enter your phone number: "))
hobby = input("What is you favorite hobby: ")

print("=== Your Profile ===")
print("Full name:" + name)
print("Age: ", age)
print("Email: ", email)
print("Phone Number: ", phone)
print("Hobby: ", hobby)
