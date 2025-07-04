import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

# Initialising scores
user_score = 0
comp_score = 0

while True:
    print("\nEnter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # choice from user
    choice = int(input("Enter your choice: "))

    # user enters valid input 
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please: '))

    # Initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user choice
    print('User choice is:', choice_name)
    print("Now it's Computer's Turn...")

    # Computer chooses random choice 
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'Scissors'

    # Print the result and update scores
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins this round! ==>")
        user_score += 1
    else:
        print("<== Computer wins this round! ==>")
        comp_score += 1

    # current scores
    print(f"Score => User: {user_score} | Computer: {comp_score}")

    # want to play aagin
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

# Final scores of game 
print("\nFinal Scores of Gameplay:")
print(f"User: {user_score} | Computer: {comp_score}")
if user_score > comp_score:
    print("Congratulations! You won the game!")
elif user_score < comp_score:
    print("Computer wins the game! Better luck next time.")
else:
    print("It's a tie overall!")

print("Thanks for playing! \n")
