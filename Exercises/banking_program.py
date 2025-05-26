# Python Banking Program

def show_balance(balance):
    print("**********************************")
    print(f"Your actual balance is ${balance:.2f}")
    print("**********************************")
def deposit():
    while True:
        user_input = input("Enter your deposit (or 'q' to cancel):$ ").lower()
        if user_input == 'q':
            return 0

        try:
            income = float(user_input)
            if income > 0:
                return income
            print("Invalid amount, please try again")
        except ValueError:
            print("Please enter a valid number")


def withdraw(balance):
    while True:
        user_input = input("Enter your withdraw (or 'q' to cancel):$ ").lower()
        if user_input == 'q':
            return 0

        try:
            amount = float(user_input)
            if amount > balance:
                print("You don't have enough amount")
            elif amount <= 0:
                print("Choose an amount bigger than 0")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number")
    return 0


def main():

    balance = 0
    is_running = True

    while is_running:
        print("**********************************")
        print("Welcome to your Banking Program!!")
        print("**********************************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("**********************************")
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                balance += deposit()
                print(f"Current balance: ${balance:.2f}")

            elif choice == 3:
                balance -= withdraw(balance)
                print(f"Current balance: ${balance:.2f}")
            elif choice == 4:
                is_running = False
            else:
                print("Enter a valid choice")
        except ValueError:
            print("Please enter a valid number (1-4)")
    print("****************************")
    print("Thank you!! have a nice day!")
    print("****************************")

if __name__ == '__main__':
    main()
