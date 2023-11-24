import random


def fight_outcome():
    # Define the probabilities
    win_probability = 0.30
    lose_probability = 0.15

    # Generate a random number between 0 and 1
    random_number = random.uniform(0, 1)

    # Determine the outcome based on the random number
    if random_number < win_probability:
        outcome = "won"
    elif random_number < win_probability + lose_probability:
        outcome = "lost"
    else:
        outcome = "remain"

    return outcome
