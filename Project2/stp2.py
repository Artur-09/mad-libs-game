import random

input("Press Enter to roll dice...")

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2, dice1 + dice2


dice1, dice2, first_roll = roll_dice()
print(f"First roll: {dice1} + {dice2} = {first_roll}")

if first_roll in [7, 11]:
    print("You Win!")

elif first_roll in [2, 3, 12]:
    print("Casino Win!")

else:
    goal = first_roll
    print("Goal number is:", goal)

    while True:
        input("Press Enter to roll dice...")
        dice1, dice2, new_roll = roll_dice()
        print(f"Roll: {dice1} + {dice2} = {new_roll}")

        if new_roll == goal:
            print("You Win!!!")
            break

        if new_roll == 7:
            print("You Lost!")
            break