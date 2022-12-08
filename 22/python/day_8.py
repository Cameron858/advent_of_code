

def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_8.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def display(data):
    for row in data:
        print(row)

def part_1(input_data):

    print(input_data)

    number_of_rows = len(input_data)
    number_of_cols = len(input_data[0])
    print(f"{number_of_rows = }, {number_of_cols = }")
    
    separated_input = []
    for row in input_data:
        separated_input.append([int(char) for char in row])
    
    display(separated_input)

    # loop through inside trees
    visible = (number_of_rows * 2) + ((number_of_cols - 2) * 2)
    print(f"{visible = }")
    for row in range(1, number_of_rows - 1):
        for col in range(1, number_of_cols - 1):
            tree = separated_input[row][col]
            print(f"Checking tree {tree} @ {row, col}")

            # left
            left = separated_input[row][:col]
            # print("Left: ", left)

            # right
            right = separated_input[row][col + 1:]
            # print("Right: ", right)

            # top
            top = []
            for i in range(row - 1, -1, -1):
                top.append(separated_input[i][col])
            # print("Top: ", top)

            # bottom
            bottom = []
            for i in range(row + 1, number_of_rows):
                bottom.append(separated_input[i][col])
            # print("Bottom: ", bottom)

            if all([x < tree for x in left]):
                visible += 1
                print(f"Found visible tree @ {row, col} {tree = }") 
            elif all([x < tree for x in right]):
                visible += 1
                print(f"Found visible tree @ {row, col} {tree = }") 
            elif all([x < tree for x in top]):
                visible += 1
                print(f"Found visible tree @ {row, col} {tree = }") 
            elif all([x < tree for x in bottom]):
                visible += 1
                print(f"Found visible tree @ {row, col} {tree = }") 
    
    print(f"{visible = }")


def count_visible_trees(tree_value, tree_list):

    for idx, tree in enumerate(tree_list):
        if tree >= tree_value:
            return len(tree_list[:idx]) + 1

    return len(tree_list)


def part_2(input_data):

    number_of_rows = len(input_data)
    number_of_cols = len(input_data[0])
    print(f"{number_of_rows = }, {number_of_cols = }")
    
    separated_input = []
    for row in input_data:
        separated_input.append([int(char) for char in row])
    display(separated_input)

    # loop through inside trees
    scenic_scores = []
    for row in range(1, number_of_rows - 1):
        for col in range(1, number_of_cols - 1):
            tree = separated_input[row][col]
            print(f"Checking tree {tree} @ {row, col}")

            # left
            left = separated_input[row][:col]
            left_count = count_visible_trees(tree, left[::-1])

            # right
            right = separated_input[row][col + 1:]
            right_count = count_visible_trees(tree, right)
        
            # top
            top = []
            for i in range(row - 1, -1, -1):
                top.append(separated_input[i][col])
            top_count = count_visible_trees(tree, top)
            
            # bottom
            bottom = []
            for i in range(row + 1, number_of_rows):
                bottom.append(separated_input[i][col])
            bottom_count = count_visible_trees(tree, bottom)
            
            s_score = left_count * right_count * top_count * bottom_count
            scenic_scores.append(s_score)
            print(f"Tree {tree} @ {row, col} has a scenic score of {s_score}")

    print(f"\nMax scenic score: {max(scenic_scores)}\n")

            

    
if __name__ == "__main__":
    input_ = load_input()
    part_2(input_)
