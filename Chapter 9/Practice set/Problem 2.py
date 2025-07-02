import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 100)  # Generate a random score

    # Step 1: Try to read the previous hi-score
    try:
        with open("Hi_score.txt", "r") as f:
            content = f.read()
            if content.strip() != "":
                hi_score = int(content.strip())
            else:
                hi_score = 0
    except FileNotFoundError:
        hi_score = 0  # If file doesn't exist, start with 0

    print("Your score:", score)
    print("High score:", hi_score)

    # Step 2: Update if new score is higher
    if score > hi_score:
        print("🎉 New High Score!")
        with open("Hi_score.txt", "w") as f:
            f.write(str(score))  # write new high score to file
    else:
        print("No new high score.")

# Call the function
game()
