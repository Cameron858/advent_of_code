

def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def sum_calories_per_elf():
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


def sum_max_three_elfs():
    """Sum the max three calories."""
    elfs = sum_calories_per_elf()
    return sum(sorted(elfs, reverse=True)[0:3])


if __name__ == '__main__':

    max_elf = max(sum_calories_per_elf())
    sum_top_three = sum_max_three_elfs()
    print(f"{max_elf = }, {sum_top_three = }")