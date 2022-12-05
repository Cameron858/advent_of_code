move_mappings = {
    "X": "Rock",
    "A": "Rock",
    "Y": "Paper",
    "B": "Paper",
    "Z": "Scissors",
    "C": "Scissors"
}

move_scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

round_scores = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_2.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def part_1():
    score = 0
    for game in lines:
        moves = game.split()
        # print(moves)

        opp = move_mappings[moves[0]]
        mine = move_mappings[moves[1]]
        # print(opp, mine)

        round = ''
        if opp == mine:
            round = 'draw'
        elif (mine == "Rock") and (opp == "Scissors"):
            round = 'win'
        elif (mine == "Rock") and (opp == "Paper"):
            round = 'lose'
        elif (mine == "Paper") and (opp == "Rock"):
            round = 'win'
        elif (mine == "Paper") and (opp == "Scissors"):
            round = 'lose'
        elif (mine == "Scissors") and (opp == "Paper"):
            round = 'win'
        elif (mine == "Scissors") and (opp == "Rock"):
            round = 'lose'
        
        # print(round)
        score += (round_scores[round] + move_scores[mine])

    print(score)


if __name__ == "__main__":
    lines = load_input()
    lines = [l.strip() for l in lines]

    new_maps = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }

    score = 0 
    for game in lines:
        moves = game.split()
        opp = move_mappings[moves[0]]
        target = new_maps[moves[1]]

        if target == "draw":
            mine = opp
        
        elif opp == "Rock":
            if target == "win":
                mine = "Paper"
            else:
                mine = "Scissors"
        
        elif opp == "Paper":
            if target == "win":
                mine = "Scissors"
            else:
                mine = "Rock"
        
        elif opp == "Scissors":
            if target == "win":
                mine = "Rock"
            else:
                mine = "Paper"
        
        game_score = round_scores[target] + move_scores[mine]
        score += game_score

    print(score)
    