def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_10_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def get_sprite_positions(x: int) -> tuple[int, int, int]:   
    return (x - 1, x, x + 1)


def display(screen):
    for r in screen:
        print(r, end='\n')


def part_2(data: list[str]):

    x = 1
    row = ''
    screen: list[str] = []
    signal_strengths: list[int] = []

    cycle_number = 1
    for inst in data:
        
        for cycle in range(2):
            print(f"{cycle_number=}")

            if cycle_number == 20 or (cycle_number - 20) % 40 == 0:
                print(f"Recording signal strength {cycle_number=}, {x=}, signal_strength={cycle_number*x}")
                signal_strengths.append(x * cycle_number)
            
            # has to be below cycle number check for signal strength
            cycle_number += 1

            if cycle_number % 40 == 0:
                print(f"Creating new row {cycle_number=}, {row}, {len(row)=}")
                screen.append(row)
                row = ''
            
            sprite_pos = get_sprite_positions(x)
            print(f"{sprite_pos=}")
            if cycle_number in sprite_pos:
                print(f"Cycle {cycle_number} is in sprite positions {x=}, {sprite_pos=}")
                row += '#'
            else:
                row += '.'

            if inst == "noop":
                break

            if inst.startswith("addx") and cycle == 1:
                _, value = inst.split(" ")
                x += int(value)

    assert len(screen) == 6
    display(screen)

    return sum(signal_strengths)

if __name__ == "__main__":
    data = load_input()
    signal_sum = part_2(data)

    assert signal_sum == 13140