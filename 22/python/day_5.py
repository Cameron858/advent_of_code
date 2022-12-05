def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_5.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    # 10 onwards to ignore the initial state
    return [l.strip() for l in input_lines][10:]


def display_stacks(stacks: list[list[str]]):
    for i, s in enumerate(stacks):
        print(i + 1, s)


def get_top_crates(stacks: list[list[str]]):
    for s in stacks:
        print(s[-1])


def decode_instructions(input_line: str):
    parts = input_line.split()
    
    procedure = {
        "count": int(parts[1]),
        "source": int(parts[3]),
        "destination": int(parts[5])
    }

    return procedure


def part_1(stacks: list[list[str]]):

    input_lines = load_input()

    for procedure in input_lines:

        instruction = decode_instructions(procedure)
        print(instruction)
        count = instruction['count']
        source_stack = instruction['source']
        target_stack = instruction['destination']

        for _ in range(count):
            crate = stacks[source_stack - 1].pop()
            stacks[target_stack - 1].append(crate)
    
    display_stacks(stacks)
    get_top_crates(stacks)


def part_2(stacks: list[list[str]]):

    input_lines = load_input()[10:]

    for procedure in input_lines:

        instruction = decode_instructions(procedure)
        print(instruction)
        count = instruction['count']
        source_stack = instruction['source']
        target_stack = instruction['destination']

        # store first n in temporary list, then append the reverse to ensure order is kept
        temp_crate_storage = []
        for _ in range(count):
            crate = stacks[source_stack - 1].pop()
            temp_crate_storage.append(crate)
        
        temp_crate_storage.reverse()       
        stacks[target_stack - 1] += temp_crate_storage
    
    display_stacks(stacks)
    get_top_crates(stacks)


if __name__ == "__main__":

    stacks = [
        ['R', 'P', 'C', 'D', 'B', 'G'],
        ['H', 'V', 'G'],
        ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
        ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
        ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
        ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
        ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
        ['C', 'M', 'D', 'B', 'F'],
        ['F', 'C', 'Q', 'G']
    ]

    part_2(stacks)