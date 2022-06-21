import random

while True:
    print("Rock Paper Scissors")
    user_action = input("Enter a choice:  ")
    possible_actions = ["R", "P", "S"]
    AI_action = random.choice(possible_actions)
    print(f"Player {user_action} : CPU {AI_action}")
    if user_action in possible_actions:
        if user_action == AI_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "R":
            if AI_action == "S":
                print("Rock smashes scissors")
            else:
                print("Paper covers rock")
        elif user_action == "P":
            if AI_action == "R":
                print("Paper covers rock ")
            else:
                print("Scissors cuts paper! You lose")
        elif user_action == "S":
            if AI_action == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

    else:
        print("invalid input")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
