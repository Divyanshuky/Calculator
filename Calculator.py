import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        user_choice = input("Enter your choice (1/2/3/4): ").lower()
        
        if user_choice == '4':
            print("Thank you for playing. Final scores:")
            print("Your score:", user_score)
            print("Computer's score:", computer_score)
            break
        
        elif user_choice not in ('1', '2', '3'):
            print("Invalid choice. Please try again.")
            continue
        
        user_choice_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice_text = user_choice_map[user_choice]
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print("\nYour choice:", user_choice_text)
        print("Computer's choice:", computer_choice)
        
        result = determine_winner(user_choice_text, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing. Final scores:")
            print("Your score:", user_score)
            print("Computer's score:", computer_score)
            break

if __name__ == "__main__":
    main()
