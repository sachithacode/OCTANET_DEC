import time

print("Please insert your CARD:")
time.sleep(5)

password =1234
pin=int(input("Enter your PIN:"))


balance=5000

if pin == password:
        while True:
            print("""
                1 == balance 
                2 == withdraw balance
                3 == deposit balance
                4 == exit
                """
            )

            try:
                option=int(input("Please enter your choice:"))

            except ValueError:
                print("Please enter valid option")
                continue

            if option == 1:
                print(f"Your balance is {balance}")
                print("==================================================")

            elif option == 2:
                withdrawal_amount=int(input("Please enter withdrawal amount"))
                if withdrawal_amount > balance:
                    print("Insufficient Balance!")

                else:
                    balance = balance - withdrawal_amount

                    print(f"{withdrawal_amount} is debited from your account")
                    print(f"your updated balance is {balance}")
                    print("==================================================")
                    print("==================================================")


            elif option == 3:
                deposit_amount=int(input("Please enter deposit amount"))
                balance = balance + deposit_amount
                print(f"{deposit_amount}is credited to your account")
                print(f"your updated balance is {balance}")
                print("==================================================")


            elif option == 4:
                print("Thank you for using ATM. Have a great day!")
                break
            else:
                print("Invalid Option, please try again")

else:
    print("Wrong PIN, please try again")

               