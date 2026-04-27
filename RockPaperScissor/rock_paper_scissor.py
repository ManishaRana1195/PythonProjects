import random

def rock_paper_scissor():
    computer_score = 0
    user_score = 0
    games = 0
    while games != 5:
        games += 1
        choice = random.choice(["rock", "paper", "scissor"])
        user_choice = input("Select from r(rock), p(paper), s(scissor): ")
        print(f"I chose: {choice[0]}, You chose: {user_choice}")
        if user_choice == choice[0]:
            continue
        
        if user_choice == 'r' :
            if choice == 'paper':
                computer_score += 1
            else :
                user_score += 1

        if user_choice == 'p':
            if choice == 'rock':
                user_score += 1
            else:
                computer_score += 1

        if user_choice == 's' :
            if choice == 'rock':
                computer_score += 1
            else:
                user_score += 1

    if(user_score == computer_score):
        print("You both tied")  
    elif user_score > computer_score:
        print(f"You won {user_score},{computer_score} ")
    else:
        print(f"Computer won {computer_score}, {user_score}")


if __name__ == "__main__":
    rock_paper_scissor()