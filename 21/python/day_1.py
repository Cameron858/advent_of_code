

def load_input():
    """Load in the data for Day 1."""
    with open(r"21\data\day_1.txt") as file_input:
        input_lines = file_input.readlines()

    return input_lines


def sliding_window(input_lines, size=2):
    index = 0
    while index < (len(input_lines) - 1):
        yield input_lines[index], input_lines[index + 1]
        index += 1


def aoc_1():
    """Count values that are higher than the previous."""
    input_lines = load_input()
    
    count_increases = 0
    for window in sliding_window(input_lines):
        first, second = window
        first = int(first)
        second = int(second)

        if second > first:
            count_increases += 1
    
    print(count_increases)


def aoc_1_1():

    input_lines = load_input()



if __name__ == "__main__":
    aoc_1()
