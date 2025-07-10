import random

imojis = {"r" : "🪨", "p" : "📃", "s" : "✂️"}

choices = ("r", "p", "s")

while True:

    user_choice = input("Rock, Paper, Scissors ?  (r/p/s): ").lower()

    if user_choice not in choices:

        print("Invalid choice")

        continue