def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_5.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]



def decode_instructions(input_line: str):
    parts = input_line.split()
    
    procedure = {
        "count": int(parts[1]),
        "source": int(parts[3]),
        "destination": int(parts[5])
    }

    return procedure


def display_stacks(stacks: list[list[str]]):
    for i, s in enumerate(stacks):
        print(i + 1, s)


def get_top_crates(stacks: list[list[str]]):
    for s in stacks:
        print(s[-1])

def part_1():

    input_lines = load_input()[10:]

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

    for procedure in input_lines:

        instructions = decode_instructions(procedure)
        print(instructions)
        count = instructions['count']
        source_stack = instructions['source']
        target_stack = instructions['destination']

        for _ in range(count):
            crate = stacks[source_stack - 1].pop()
            stacks[target_stack - 1].append(crate)
    
    display_stacks(stacks)
    get_top_crates(stacks)
            
def part_2():
    input_lines = load_input()[10:]

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

    for procedure in input_lines:

        
        instructions = decode_instructions(procedure)
        print(instructions)
        count = instructions['count']
        source_stack = instructions['source']
        target_stack = instructions['destination']

        temp = []
        for _ in range(count):
            crate = stacks[source_stack - 1].pop()
            temp.append(crate)
        
        temp.reverse()       
        stacks[target_stack - 1] += temp
    
    display_stacks(stacks)
    get_top_crates(stacks)


if __name__ == "__main__":
    part_2()