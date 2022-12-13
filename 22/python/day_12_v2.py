import string


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_12_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def get_adjacent_positions(check_position: tuple[int, int], max_rows=41, max_cols=95):
    """
    
    (20, 0) -> [(19, 0), (20, 1), (21, 0)]
    """
    row, col = check_position
    max_rows -= 1
    max_cols -= 1

    positions = []
    for r in (row - 1, row + 1):
        if 0 <= r <= max_rows:
            positions.append((r, col))
    
    for c in (col - 1, col + 1):
        if 0 <= c <= max_cols:
            positions.append((row, c))

    print(f"Found {positions = } for {check_position = }, ({max_rows=}, {max_cols=})")
    return positions


def get_char(heights: list[list[str]], position: tuple[int, int]):
    return heights[position[0]][position[1]]


def part_1(data: list[str]):
    
    number_of_moves = 0
    locations_visited = set()

    # transform input
    heights = [[c for c in row.strip()] for row in data]
    n_rows = len(heights)
    n_cols = len(heights[0])
    
    start_position = (0, 0)
    end_position = (0, 0)
    # find start and end point
    for r_idx, row in enumerate(heights):
        for c_idx, elevation in enumerate(row):

            if elevation == "S":
                start_position = (r_idx, c_idx)
            
            if elevation == "E":
                end_position = (r_idx, c_idx)
    
    print(f"{start_position = }, {end_position = }")

    character_moves: dict[str, list[str]] = {
        "S": ['a']
    }
    # map possible positons for each letter
    letters = string.ascii_lowercase
    for index, char in enumerate(letters[0:-1]):
        if index == 0:
            character_moves[char] = [char, letters[index + 1]]
        else:
            character_moves[char] = [letters[index - 1], char, letters[index + 1]]
    # add end position to possible move list
    character_moves["z"] = ['y', 'E']
    print(character_moves)

    path = [start_position]
    while path:
        print(f"\n{path = }")
        position = path.pop(0)
        number_of_moves += 1
        current_char = get_char(heights, position)

        if position == end_position:
            print(f"\n\nThe end has been found @ {pos}")
            print(f"{number_of_moves = }")
            print(len(locations_visited))
            exit(0)
        
        print(f"Current position {position}")
        for pos in get_adjacent_positions(position, n_rows, n_cols):
            print(f"Checking {pos=}")
              
            # check if visited before
            if pos in locations_visited:
                print(f"{pos} has been visited")
                continue
            
            # check if valid move
            if get_char(heights, pos) not in character_moves[current_char]:
                print(f"{pos} is not a valid move. Tried to move from {current_char} to {get_char(heights, pos)}")
                continue
            
            print(f"Found viable pos {pos}")
            locations_visited.add(pos)
            path.append(pos)
    
    print(f"The end was not found.")
    print(f"{number_of_moves = }")
    

if __name__ == "__main__":
    data = load_input()
    part_1(data)