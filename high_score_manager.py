
# High Score Manager
# Developed by ZeroTrustX

print("Welcome to the Score Manager") 

file_name = 'high_scores.txt'

def read_scores():
    try:
        with open(file_name, 'r') as file:
            scores = []
            for line in file:
                name, score = line.strip().split(',')
                scores.append((name, int(score)))
            return scores
    except FileNotFoundError:
        return []

def write_scores(scores):
    with open(file_name, 'w') as file:
        for name, score in scores:
            file.write(f"{name},{score}\n")

def add_or_update_score(scores, player_name, player_score):
    player_found = False
    for i in range(len(scores)):
        name, score = scores[i]
        if player_name == name:
            if player_score > score:
                scores[i] = (player_name, player_score)
            player_found = True
            break
    if not player_found:
        scores.append((player_name, player_score))

def search_score(scores, player_name):
    for name, score in scores:
        if player_name == name:
            return score
    return None

scores = read_scores()

while True:
    print("\nMenu:")
    print("1. Add User Score")
    print("2. Search Score")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        player_name = input("Enter player name: ")
        score_input = input("Enter player score: ")
        try:
            player_score = int(score_input)
            add_or_update_score(scores, player_name, player_score)
            write_scores(scores)
            print("Score added/updated successfully.")
        except ValueError:
            print("Invalid score. Please enter a number.")
    elif choice == '2':
        player_name = input("Enter player name: ")
        score = search_score(scores, player_name)
        if score is not None:
            print(f"Player: {player_name}, Score: {score}")
        else:
            print("Player not found.")
    elif choice == '3':
        print("Exit program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
