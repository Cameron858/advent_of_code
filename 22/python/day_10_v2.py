def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_10_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def part_2(data: list[str]):

    x = 1
    row = ''
    signal_strengths: list[int] = []

    cycle_number = 1
    for inst in data:
        
        for cycle in range(2):
            
            if cycle_number == 20 or (cycle_number - 20) % 40 == 0:
                print(f"Recording signal strength {cycle_number=}, {x=}, signal_strength={cycle_number*x}")
                signal_strengths.append(x * cycle_number)
            
            cycle_number += 1

            if inst == "noop":
                break

            if inst.startswith("addx"):
                i, value = inst.split(" ")
                
                if cycle == 1:
                    x += int(value)


    
    print(signal_strengths, sum(signal_strengths))

if __name__ == "__main__":
    data = load_input()
    part_2(data)