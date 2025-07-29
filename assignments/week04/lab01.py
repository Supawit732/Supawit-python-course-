
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Supawit Leelachayakul", 19, "Samutparkan", "Thailand")  # name, age, city, country
    hobbies = ["Watching football"]
    name, age, city, country = person
    # Your code here
    while True:
        print("=" * 40)
        print("\tPersonal Information Manager")
        print("=" * 40)
        print("\n1. Display all information")
        print("2. Add new hobbies")
        print("3. Remove hobbies") 
        print("4. Upate age")
        print("5. Exit")
        choice = int(input("Choose option: "))
        if choice == 1:
            print("===== Personal Information =====")
            print(f"Name:{name}\n Age:{age}\n City:{city}\n Country:{country}\n Hobby:{hobbies}")
        elif choice == 2:
            new_hobby = input("Enter you hobby: ")
            hobbies.append(new_hobby)
            print(hobbies)
        elif choice == 3:
            delete = input("What hobby do yo want to delete: ")
            hobbies.remove(delete)
            print(hobbies)
        elif choice == 4:
            person_list = list(person)
            age = int(input("Enter your age: "))
            person_list[1] = age
            person = tuple(person_list)
            print(f"Name:{name}\n Age:{age}\n City:{city}\n Country:{country}\n Hobby:{hobbies}")
        elif choice == 5:
            break
        again = input("Would you like to perform another action? (Enter 'Y' to continue, any other key to exit): ")
        if again != "Y":
            print("Thank you for using")
            break  
        
        pass

if __name__ == "__main__":
    personal_info_manager()

