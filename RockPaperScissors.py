import random

emojis = {"r" : "🪨", "p" : "📃", "s" : "✂️"}

choices = ("r", "p", "s")

user_score = 0

computer_score = 0

while True:

    user_choice = input("Rock 🪨, Paper 📃, Scissors ✂️ ?  (r/p/s): ").lower()

    if user_choice not in choices:

        print("Invalid choice")

        continue

    computer_choice = random.choice(choices)

    print(f"Your choice : {emojis[user_choice]}")

    print(f"Computer choice : {emojis[computer_choice]}")

    if user_choice == computer_choice:

        print("Tie!")
        
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")) :

        print("You Win")

        user_score += 1

    else:

        print("You Lose")

        computer_score += 1

    print(f"Score : Your Score: {user_score}  -  Computer Score: {computer_score}")

    should_continue = input("Play?  (y / n): ").lower()

    if should_continue not in ("y"or"yes"):

        print("Thanks for Playing!")

        break