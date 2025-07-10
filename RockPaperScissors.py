import random

emojis = {"r" : "🪨", "p" : "📃", "s" : "✂️"}

choices = ("r", "p", "s")

while True:

    user_choice = input("Rock, Paper, Scissors ?  (r/p/s): ").lower()

    if user_choice not in choices:

        print("Invalid choice")

        continue

    computer_choice = random.choice(choices)

    print(f"Your choice : {emojis[user_choice]}")

    print(f"Computer choice : {emojis[computer_choice]}")