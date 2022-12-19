def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_10.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


class CRT:

    def __init__(self) -> None:
        self.x_register = 1
        self.cycle_number = 0
        self.signal_strengths: list[int] = []

        # part 2
        self.screen = [['.' for _ in range(40)] for _ in range(6)]
    
    def tick(self):
        self.cycle_number += 1

        if self.cycle_number % 40 == 20:
            print(f"Recording signal strength {self.cycle_number=} {self.x_register=}")
            self.signal_strengths.append(self.cycle_number * self.x_register)
        
        if self.cycle_number % 40 in self.get_sprite_positions():
            row = self.cycle_number // 40
            col = self.cycle_number % 40
            self.screen[row][col] = '#'
            print(f"The sprite is at {self.x_register}, in positions {self.get_sprite_positions()}")
    
    def add_x(self, value: int):
        # print(f"Adding {value=}")
        self.x_register += value
    
    def sum_signal_strengths(self):
        total_signal_strength = sum(self.signal_strengths)
        print(f"The total sum of the signal strengths is {total_signal_strength}")
        return total_signal_strength
    
    def get_sprite_positions(self):
        pos = self.x_register
        return (pos - 1, pos, pos + 1)
    
    def display_screen(self):
        for row in self.screen:
            print("".join(row))


def part_1(data: list[str]):

    crt = CRT()

    for instruction in data:
        
        if instruction.startswith("noop"):
            crt.tick()
        
        if instruction.startswith("addx"):
            crt.tick()
            value = int(instruction.split(" ")[1])
            crt.add_x(value)
            crt.tick()

    # 13140 for example, 12540 for my input
    # assert crt.sum_signal_strengths() == 13140
    print(crt.signal_strengths)


def part_2(data: list[str]):

    crt = CRT()

    for instruction in data:
        
        if instruction.startswith("noop"):
            crt.tick()
        
        if instruction.startswith("addx"):
            crt.tick()
            value = int(instruction.split(" ")[1])
            crt.add_x(value)
            crt.tick()
    
    crt.display_screen()


if __name__ == "__main__":
    data = load_input()
    part_1(data)
    part_2(data)
