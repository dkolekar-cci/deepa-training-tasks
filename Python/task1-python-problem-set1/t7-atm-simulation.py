def atm_simulation():
    balance = 10000.0

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("Current Balance: Rs" + str(balance))

        elif choice == '2':
            amount = input("Enter amount to deposit: ")
            if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue
            balance += float(amount)
            print("Deposited successfully.")

        elif choice == '3':
            amount = input("Enter amount to withdraw: ")
            if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue
            amount = float(amount)
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print("Withdrawal successful.")

        elif choice == '4':
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid option. Please try again.")

atm_simulation()