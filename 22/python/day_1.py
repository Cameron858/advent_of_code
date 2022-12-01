

def load_input():
    """Load in the data for Day 1."""
    try:
        with open(r"22\data\day_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def aoc_1():
    """Calculate the calories per elf."""
    input_lines = load_input()    

    calories_per_elf = []
    sum = 0
    for value in input_lines:
        if value == '\n':
            calories_per_elf.append(sum)
            sum = 0
        else:
            calories = int(value)
            sum += calories
    
    return calories_per_elf


def aoc_1_2():
    """Sum the max three calories."""
    elfs = aoc_1()
    return sum(sorted(elfs, reverse=True)[0:3])


if __name__ == '__main__':

    max_elf = max(aoc_1())
    sum_top_three = aoc_1_2()
    print(f"{max_elf = }, {sum_top_three = }")