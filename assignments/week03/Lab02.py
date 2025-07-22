# Complete this ATM simulation
print("=" * 40)
print("\t\tATM Program")
print("=" * 40)
pin = "1234"
balance = 1000
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = int(input("Choose option: "))
        if choice == 1:
            print("Your balance is ",balance)
        elif choice == 2:
            withdraw =int(input("Enter the amount you want to Withdraw: "))
            if balance >= withdraw:
                balance = balance - withdraw
                print("Your balance is ",balance)
            else:
                print("Your account has insufficient funds.")
        elif choice == 3:
            deposit = int(input("Enter the amount you want to Deposit: "))
            if deposit > 0:
                balance = balance + deposit
                print("Your balance is ",balance)
            else:
                print("Invaild number")
        elif choice == 4:
            ("Thank you for using ")
            break
        else :
            print("Invalid option")
        again = input("Would you like to perform any other transactions?(Y/anykey): ")
        if again != "Y":
            print("Thank you for using")
            break         
else:
    print("Invalid PIN")

