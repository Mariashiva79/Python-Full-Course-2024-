# slot machine 🎰
import random

row = []
def spin_row():
    symbols_row = ["🍒", "🍉", "🍋", "🔔", "🌟"]
    row.clear()
    for _ in range(3):
        row.append(random.choice(symbols_row))
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(bet, balance):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            bet *= 2
            balance += bet
        elif row[0] == "🍉":
            bet *= 3
            balance += bet
        elif row[0] == "🍋":
            bet *= 4
            balance += bet
        elif row[0] == "🔔":
            bet *= 10
            balance += bet

        elif row[0] == "🌟":
            bet *= 20
            balance += bet
        print("You win!!" + (" Excellent!!" if row[0] == "🌟" else ""))
        print(f"\nYour current balance is ${balance:.2f}")
        return balance, True

    else:
        print("You lose!")
        print(f"Your current balance is ${balance:.2f}")
        while True:
            response = input("You lose your bet, play again (Y/N)?: ").upper()
            if response == "Y":
                return balance, True
            elif response == "N":
                return balance, False
            print("Please enter Y or N")


def main():
    balance = 100
    playing = True
    while playing:
        if balance <= 0:
            print("You have not funds")
            break
        print("****************************")
        print("Welcome to slot machine 🎰!!")
        print("Symbols: 🍒 🍉 🍋 🔔 🌟")
        print("****************************")

        print(f"\nYour current balance is ${balance:.2f}")
        try:
            bet = float(input("Place your bet amount:$ "))
            if bet > balance:
                print("Haven´t got enough amount")
                continue
            elif bet <= 0:
                print("Enter a bet bigger than 0")
                continue
            else:
                print("Spinning...")
                spin_row()
                balance -= bet
                balance, playing = get_payout(bet, balance)

        except ValueError:
            print("Enter a valid number")

    print("Thank you for playing with us!!")

if __name__ == "__main__":
    main()


