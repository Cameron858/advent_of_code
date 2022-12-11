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


def display_screen(screen: list[str]) -> None:
    for row in screen:
        print(row)


def get_sprite_positions(x: int) -> tuple[int, int, int]:   
    return (x - 1, x, x + 2)


def part_1(data: list[str]):

    print(data)
    x = 1
    signal_strengths = []
    screen: list[str] = []

    big_row = ''

    cycle_number = 1
    for inst in data:
        # print(f"{cycle_number=}")

        if inst == "noop":
            cycle_number += 1

            if cycle_number in get_sprite_positions(x):
                big_row += '#'
                if len(big_row) == 40:
                    screen.append(big_row)
                    big_row = ''
            else:
                big_row += '.'
                if len(big_row) == 40:
                    screen.append(big_row)
                    big_row = ''
            
            if cycle_number == 20 or (cycle_number - 20) % 40 == 0:
                        print(f"Recording signal strength {cycle_number=}, {x=}, signal_strength={cycle_number*x}")
                        signal_strengths.append(x * cycle_number)

        else:
            inst, value = inst.split(" ")

            if inst == "addx":

                for cycle in range(2):
                    # print(f"Adding {value} to x")
                    if cycle_number in get_sprite_positions(x):
                        big_row += '#'
                        if len(big_row) == 40:
                            screen.append(big_row)
                            big_row = ''
                    else:
                        big_row += '.'
                        if len(big_row) == 40:
                            screen.append(big_row)
                            big_row = ''
                    
                    cycle_number += 1
                    
                    if cycle == 1:
                        x += int(value)
        
                    if cycle_number == 20 or (cycle_number - 20) % 40 == 0:
                        print(f"Recording signal strength {cycle_number=}, {x=}, signal_strength={cycle_number*x}")
                        signal_strengths.append(x * cycle_number)

    
    print(f"Recorded signals: {signal_strengths}")
    print(f"Signal sum: {sum(signal_strengths)}")

    display_screen(screen=screen)
    

if __name__ == "__main__":
    data = load_input()
    part_1(data)