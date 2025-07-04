import random

print("Let's play best of 5 of Rock Paper Scissors \n Choose rock, paper, or scissors. ")

user_score = 0
computer_score = 0

# List of choices
options = ["rock", "paper", "scissors"]

while user_score < 3 and computer_score < 3:
    user_choice = input().lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice not in options:
        print("Invalid option. Type either Rock, Paper, or Scissors.")
        continue

    if user_choice == computer_choice:
        print("You and the computer tied, try again")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        print(
            f" You win this round! Your score is {user_score} and the computer's is {computer_score}.")
    else:
        computer_score += 1
        print(
            f" Computer wins this round! Your score is {user_score} and the computer's is {computer_score}.")
    if user_score < 3 and computer_score < 3:
        print("Choose rock, paper, or scissors.")

if user_score == 3:
    print(f"🎊 Congrats, you won the game {user_score} to {computer_score}!")
else:
    print(f"😓 You lost the game {user_score} to {computer_score}. ")
