Dice Game (Craps-like)
A simple command-line Python game based on rolling two dice. The logic is inspired by the classic casino game craps.

📌 Description
This program simulates rolling two six-sided dice and determines the outcome based on the following rules:

First Roll:
7 or 11 → 🎉 You win
 
2, 3, or 12 → 💀 Casino wins (you lose)

Any other number → becomes your goal number

Subsequent Rolls:
If you roll the goal number again → 🎉 You win

If you roll a 7 → ❌ You lose

Otherwise → keep rolling until one of the above happens

▶️ How to Run
Make sure you have Python 3 installed

Save the code into a file, for example:

dice_game.py
Run the program in your terminal:

python dice_game.py
🎮 How to Play
Press Enter to roll the dice

Follow the results displayed in the console

The game will automatically tell you if you win or lose

🧠 How It Works
Uses the built-in random module to generate dice rolls

The roll_dice() function returns the sum of two dice (2–12)

Game logic is handled with conditional statements and a loop

💡 Possible Improvements
Ideas to expand the project:

Add a win/loss counter

Implement a betting system 💰

Build a graphical interface (e.g., with tkinter)

Store game history or statistics
