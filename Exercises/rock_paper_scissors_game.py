# ⭐ rock, paper, scissors game 🗿
import random

options = ("rock", "paper", "scissors")
playing = True
score = 0
total_score = []

print("Wellcome \U0001F389!!: \n 'Paper \U0001F4C4, Scissors \u2702\ufe0f and Rock \U0001FAA8' Game!!")
print()

while playing:

    player = None
    computer = random.choice(options)
    total_score.append(score)

    while player not in options:
        player = input("Enter your option (rock\U0001FAA8, paper\U0001F4C4, scissors\u2702\ufe0f): ").lower()
    print()
    print("---------------------")
    if player == "rock":
        print(f"You: {player} \U0001FAA8")
    elif player == "scissors":
        print(f"You: {player} \u2702\ufe0f")
    else:
        print(f"You: {player} \U0001F4C4")

    if computer == "rock":
        print(f"Computer: {computer} \U0001FAA8")
    elif computer == "scissors":
        print(f"Computer: {computer} \u2702\ufe0f")
    else:
        print(f"Computer: {computer} \U0001F4C4")
    print("---------------------")
    if player == computer:
        print("It is a tie!!")
        score += 0
        print("---------------------")
    elif player == "rock" and computer == "scissors":
        print("You win!!")
        score += 1
        print("---------------------")
    elif player == "paper" and computer == "rock":
        print("You win!!")
        score += 1
        print("---------------------")
    elif player == "scissors" and computer == "paper":
        print("You win!!")
        score += 1
        print("---------------------")
    else:
        print("You lose :-( ")
        score -= 1
        print("---------------------")

    play_again = input("Try again? (y/n): ").lower()
    if not play_again == "y":
        total_score = score
        playing = False
        print("---------------------")

if total_score < 0:
    print("****************************************")
    print(f"Your total score is {total_score}, computer win!")
    print("****************************************")

elif total_score > 0:
    print("****************************************")
    print(f"Your total score is {total_score}, You win!")
    print("****************************************")

else:
    print("****************************************")
    print(f"Your total score is {total_score}, It is a tie!")
    print("****************************************")
print()
print("Thank you for play!!")
