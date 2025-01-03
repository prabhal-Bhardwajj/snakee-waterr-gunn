import random
import csv
import os
#///////////////////////////////////////////////////////////

FILE_PATH = 'game_results.csv'
GAME_DICTIONARY = {
    1: ["Water", "w", "W", "WATER", 1, "water"],
    2: ["Snake", "s", "S", "SNAKE", 2, "snake"],
    3: ["Gun", "G", "g", "GUN", 3, "gun"]
}

DIFFICULTY_STAGE = {
    -2: "Very Easy", -1: "Easy", 0: "Normal", 1: "Hard", 2: "Very Hard",
    "Very Easy": "Very Easy", "Easy": "Easy", "Normal": "Normal",
    "Hard": "Hard", "Very Hard": "Very Hard"
}

# Function for writing results to a file
def save_results(file_path, rounds, difficulty_level, user_score, comp_score, user_fav, comp_fav):
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, mode='a+', newline='') as file:
        writer = csv.writer(file)
        
        # initially it will create the file and then add these columns
        
        if not file_exists:
            writer.writerow(["Number of Rounds", "Difficulty Level", "User Wins", "Computer Wins", "User Favorite Choice", "Computer Favorite Choice"])
        #append to the end of the file.
        writer.writerow([rounds, difficulty_level, user_score, comp_score, user_fav, comp_fav])
    print(f"Game results saved to '{file_path}'.")

# Function to get computer choice based on difficulty
def difficulty_stage(player_choice, difficulty):
    winning_choice = {1: 2, 2: 3, 3: 1}  
    losing_choice = {1: 3, 2: 1, 3: 2}  
    # winning weights probablity
    
    probabilities = {
        "Very Easy": [5, 95],
        "Easy": [25, 75],
        "Normal": [50, 50],
        "Hard": [75, 25],
        "Very Hard": [95, 5]
    }
    return random.choices([losing_choice[player_choice], winning_choice[player_choice]], weights=probabilities[difficulty])[0]

# Function for the game logic
def game_to():
    while True:
        print("\nWelcome to the Snake, Water, Gun Game!\n")
        print('''We have the following difficulty levels:
            - Very Easy (-2)
            - Easy (-1)
            - Normal (0)
            - Hard (1)
            - Very Hard (2)
        Please select your difficulty level.
        -------------------------''')
#//////////////////////////////////////////////////////////////////////////////////////
        while True:
            difficulty_input = input("Choose a difficulty level : ").strip()
            try:
                difficulty_value = int(difficulty_input)
                if difficulty_value in DIFFICULTY_STAGE:
                    difficulty_level = DIFFICULTY_STAGE[difficulty_value]
                    break
            except ValueError:
                if difficulty_input in DIFFICULTY_STAGE:
                    difficulty_level = DIFFICULTY_STAGE[difficulty_input]
                    break
            print("Invalid difficulty. Choose from Very Easy, Easy, Normal, Hard, Very Hard or their integer equivalents (-2 to 2).")
#//////////////////////////////////////////////////////////////////////////////////
        while True:
            try:
                rounds = int(input("Enter the number of rounds you want to play: "))
                if rounds > 0:
                    break
                else:
                    print("Number of rounds must be positive.")
            except ValueError:
                print("Invalid input! Please enter a positive integer.")

        your_score, comp_score = 0, 0
        user_choices, comp_choices = [], []
# ///////////////////////////////////////////////////////////////
        for i in range(1, rounds + 1):
            print(f"\n--- Round {i} ---")
            while True:
                user_input = input('''Enter your choice:
                    1 : Water
                    2 : Snake
                    3 : Gun
                    (Press Q to Quit)
                    --> ''').strip()
                if user_input.lower() == 'q':
                    print("You chose to quit the game. Exiting...")
                    return
                try:
                    user_choice = int(user_input)
                    if user_choice in GAME_DICTIONARY:
                        break
                except ValueError:
                    for choice_key, choice_values in GAME_DICTIONARY.items():
                        if user_input.lower() in choice_values:
                            user_choice = choice_key
                            break
                    else:
                        print("Invalid input! Try again.")
                        continue
                    break

            computer_choice = difficulty_stage(user_choice, difficulty_level)
            user_choices.append(GAME_DICTIONARY[user_choice][0])
            comp_choices.append(GAME_DICTIONARY[computer_choice][0])

            print(f"Your choice: {GAME_DICTIONARY[user_choice][0]}")
            print(f"Computer's choice: {GAME_DICTIONARY[computer_choice][0]}")

            if user_choice == computer_choice:
                print("It's a tie!")
                your_score += 1
                comp_score += 1
            elif (user_choice == 1 and computer_choice == 2) or\
                (user_choice == 2 and computer_choice == 3) or\
                (user_choice == 3 and computer_choice == 1):
                print("You win this round!")
                your_score += 2
            else:
                print("You lose this round!")
                comp_score += 2

            print(f"Current Scores -> You: {your_score}, Computer: {comp_score}")

        print("\n=== Game Over ===")
        print(f"Your final score: {your_score}")
        print(f"Computer's final score: {comp_score}")

        user_fav = max(set(user_choices), key=user_choices.count)
        comp_fav = max(set(comp_choices), key=comp_choices.count)
        save_results(FILE_PATH, rounds, difficulty_level, your_score, comp_score, user_fav, comp_fav)

        while True:
            play_again = input("\nPress C to continue playing or Q to quit: ").strip().lower()
            if play_again == 'c':
                break
            elif play_again == 'q':
                print("Thank you for playing! Goodbye!")
                return
            else:
                print("Invalid input. Please press C to continue or Q to quit.")

# Run the game
game_to()

# ////////////////////////////////////////////////////////////////////////////////////////
'''
ANY SUGGESTIONS THEN DROP HERE.



'''
