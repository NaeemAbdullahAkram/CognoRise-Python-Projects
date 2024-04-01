import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            if sides <= 0:
                print("Number of sides must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                print("Number of rolls must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f"\nRolling a {sides}-sided dice {num_rolls} times...\n")
    for i in range(num_rolls):
        result = roll_dice(sides)
        print(f"Roll {i + 1}: {result}")

    play_again = input("\nDo you want to roll again? (yes/no): ").lower()
    if play_again == "yes":
        main()

if __name__ == "__main__":
    main()
