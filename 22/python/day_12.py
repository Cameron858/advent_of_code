import string
import time
import random
import math


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_12.txt") as file_input:
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


def find_highest_char(char_list: list[str]):
    letters = string.ascii_lowercase[::-1]
    letters = 'E' + letters + 'S'
    print(letters)

    for i, c in enumerate(letters):
        if c in char_list:
            return (i, c)

def part_1(data: list[str]):
    
    number_of_moves = 0
    locations_visited: list[tuple[int, int]] = []

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


    current_position = start_position
    current_char = get_char(heights, current_position)

    while current_char != "E":
    # for _ in range(10):

        locations_visited.append(current_position)
        print(locations_visited)

        print(f"{current_position = }, {current_char = }")
        adjacent_locations = get_adjacent_positions(current_position, n_rows, n_cols)
        print(f"{adjacent_locations = }")
        adjacent_chars = [get_char(heights, pos) for pos in adjacent_locations]
        print(f"{adjacent_chars = }")

        # try to find a char that is one higher than current
        one_higher_char = character_moves[current_char][-1]
        try:
            one_higher_index = adjacent_chars.index(one_higher_char)
            print(f"Found {one_higher_char = } @ {one_higher_index = }")
        except ValueError:
            one_higher_index = None
            print(f"Could not find higher char in {adjacent_chars}")
        
        # if there is one higher then move to it, else check what we can move to
        if one_higher_index is not None:
            current_position = adjacent_locations[one_higher_index]
            current_char = get_char(heights, current_position)
            print(f"Moving to {current_position}, ({current_char})")
        else:
            is_char_in_move_set = [char in character_moves[current_char] for char in adjacent_chars]
            print(f"{is_char_in_move_set = }")
            possible_move_locations = [pos for pos, check in zip(adjacent_locations, is_char_in_move_set) if check]
            print(f"{possible_move_locations = }")

            unvisited_locations = [pos for pos in possible_move_locations if pos not in locations_visited]
            print(f"{unvisited_locations = }")

            if unvisited_locations:
                current_position = unvisited_locations[-1]
                current_char = get_char(heights, current_position)
                print(f"Moving to {current_position}, ({current_char})")
            else:
                print(f"Found no unvisited locations")
                possible_move_locations = sorted(possible_move_locations, key=lambda x: x[1], reverse=True)
                current_position = locations_visited.pop(-1)
                current_char = get_char(heights, current_position)
                print(f"Moving to {current_position}, ({current_char})")
            
        print("")
        number_of_moves += 1
        time.sleep(0)

    print(f"{number_of_moves = }")


if __name__ == '__main__':
    data = load_input()
    part_1(data)
