"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

name = "John Doe"
age = "25"
phone = "9876543210"

nameFlag = True
for char in name:
    print(char, char.isalpha())
    if char.isalpha() or char == " ":
        nameFlag = True
    else:
        nameFlag = False
        break
ageFlag = True
if int(age) < 18 or int(age) > 65:
    ageFlag = False

phoneFlag = True
if len(phone) != 10:
    phoneFlag = False
else:
    for char in phone:
        if char.isdigit() == False:
            phoneFlag = False
            break
print("Validation Results:")

if nameFlag:
    print("Valid (contains only letters and spaces)")
else:
    print("Invalid(not contains only letters and spaces)")
if ageFlag:
    print(f"Valid ({age} years old)")
else:
    print("Invalid (not 18-65 years old)") 
if phoneFlag:
    print("Valid (10-digit number)")
else:
    print("Invalid (not 10-digit number)")   

print("Name : %s" % name.upper())
#print(name.upper(), name.lower(), name.title(),name.capitalize())
if int(age) >= 18 and int(age) <= 30:
    print("Age Group : Young Adult")
else:
    print("Age Group : not Young Adult")
print(f"Phone : +66{phone}")