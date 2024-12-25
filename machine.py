#Python Slot Machine

import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '🌟' ]

    results = []
    for symbol in range (3):
        results.append(random.choice(symbols))
    return results 

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🌟':
            return bet * 20

def main():
    balance = 100

    print (" ********************** ")
    print (" Welcome to Python Slots ")
    print (" Symbols: 🍒 🍉🍋🔔🌟 ")
    print (" ********************** ")

    while balance > 0:
        print (f"Current balance: ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int (bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print ("spinning...\n")
        print_row(row)

        payout = get_payout( row, bet)



    

if __name__ == '__main__':
    main()