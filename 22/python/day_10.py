def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_10_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def make_row(lit: int) -> str:
    row = ['.' for _ in range(40)]
    row[lit] = '#'
    return row


def display_screen(screen: list[list[str]]) -> None:
    for row in screen:
        print(row)


def part_1(data: list[str]):

    print(data)
    x = 1
    signal_strengths = []
    screen: list[list[str]] = []

    cycle_number = 1
    for inst in data:
        # print(f"{cycle_number=}")

        if inst == "noop":
            cycle_number += 1

            if cycle_number == 20 or (cycle_number - 20) % 40 == 0:
                        print(f"Recording signal strength {cycle_number=}, {x=}, signal_strength={cycle_number*x}")
                        signal_strengths.append(x * cycle_number)
            
        else:
            inst, value = inst.split(" ")

            if inst == "addx":

                for cycle in range(2):
                    cycle_number += 1
                    # print(f"Adding {value} to x")
                    
                    if cycle == 1:
                        x += int(value)
        
                    if cycle_number == 20 or (cycle_number - 20) % 40 == 0:
                        print(f"Recording signal strength {cycle_number=}, {x=}, signal_strength={cycle_number*x}")
                        signal_strengths.append(x * cycle_number)
        
        
        
        # print(f"{x=}")
    
    print(f"Recorded signals: {signal_strengths}")
    print(f"Signal sum: {sum(signal_strengths)}")
            


if __name__ == "__main__":
    data = load_input()
    part_1(data)