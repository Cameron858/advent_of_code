

def load_input():
    """Load in the data."""
    try:
        with open(r"21\data\day_2.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def part_1(input_data: list[str]):
    print(input_data)

    horizontal_position = 0
    depth = 0

    for command in input_data:

        command = command.strip().split()

        if command[0] == "forward":
            horizontal_position += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
        else:
            print(f"Unknown command found: {command[0]}. Doing nothing.")
    
    print(f"Part 2: Reached destination: {horizontal_position = }, {depth = } {horizontal_position * depth}")



def part_2(input_data):
    print(input_data)

    horizontal_position = 0
    depth = 0
    aim = 0

    for command in input_data:

        command = command.strip().split()

        if command[0] == "forward":
            horizontal_position += int(command[1])
            depth += (aim * int(command[1]))
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
        else:
            print(f"Unknown command found: {command[0]}. Doing nothing.")
    
    print(f"Part 2: Reached destination: {horizontal_position = }, {depth = } {horizontal_position * depth}")


if __name__ == "__main__":
    input_data = load_input()
    part_1(input_data)
    part_2(input_data)