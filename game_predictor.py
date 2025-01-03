import pandas as pd
from collections import Counter

# Load data
try:
    data = pd.read_csv('game_results.csv')  
    print(data)
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
    exit()

# Analyze frequency of computer choices per difficulty
freq_analysis = data.groupby('Difficulty Level')['Computer Favorite Choice'].apply(Counter)
print(freq_analysis)

# Suggestion logic (based on frequency or machine learning)
def suggest_choice(difficulty_level):
    try:
        # Get the most common choice for the difficulty level
        common_choice = freq_analysis[difficulty_level].most_common(1)[0][0]
        # Map to the winning choice
        winning_choice = {'Water': 'Gun', 'Snake': 'Water', 'Gun': 'Snake'}
        return winning_choice[common_choice]
    except KeyError:
        return f"No data available for difficulty level: {difficulty_level}"
    except IndexError:
        return f"No computer choices recorded for difficulty level: {difficulty_level}"

# Example usage
print(suggest_choice('Easy'))
