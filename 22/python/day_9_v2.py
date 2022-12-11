

def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_9.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


class Knot:
    
    def __init__(self, x, y) -> None:
        self.x: int = x
        self.y: int = y
        self.pos: tuple[int, int] = (self.x, self.y)

    def __repr__(self) -> str:
        return f"Knot(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Knot(x={self.x}, y={self.y})"

    def __sub__(self, other: 'Knot') -> tuple[int, int]:
        return (self.x - other.x, self.y - other.y)

    def move(self, movement_vector: tuple[int, int]):
        self.x += movement_vector[0]
        self.y += movement_vector[1]

    def is_adjacent(self, other: 'Knot') -> bool:
        """Return true if self is adjacent with other `Knot`"""
        positional_difference = other - self
        return positional_difference[0] in [-1, 0, 1] and positional_difference[1] in [-1, 0, 1]
    
    
class RopeGrid:

    def __init__(self, n_knots) -> None:

        assert n_knots >= 2

        self.start_x = 0
        self.start_y = 0
        self.knots = [Knot(x=self.start_x, y=self.start_y) for _ in range(n_knots)]
        self.tail_positions = set()
    
    def move_head(self, x_diff, y_diff):
        head = self.knots[0]
        head.move((x_diff, y_diff))

    def record_tail_position(self):
        tail = self.knots[-1]
        self.tail_positions.add((tail.x, tail.y))
    
    def update_body(self):

        for number, knot in enumerate(self.knots[1:]):

            parent = self.knots[number]

            if not knot.is_adjacent(other=parent):
                position_difference = parent - knot

                try:
                    x_diff = int(position_difference[0] / abs(position_difference[0]))
                except ZeroDivisionError:
                    x_diff = 0

                try:
                    y_diff = int(position_difference[1] / abs(position_difference[1]))
                except ZeroDivisionError:
                    y_diff = 0
                
                knot.move((x_diff, y_diff))
            
            self.record_tail_position()
    
    def simulate(self, data: list[str]) -> int:

        for motion in data:
            direction, distance = motion.split(" ")
            distance = int(distance)

            for n in range(distance):

                if direction == "R":
                    self.move_head(1, 0)
                elif direction == "L":
                    self.move_head(-1, 0)
                elif direction == "U":
                    self.move_head(0, 1)                
                elif direction == "D":
                    self.move_head(0, -1)

                self.update_body()
        
        print(f"The tail touched {len(self.tail_positions)} unique locations.")

        return len(self.tail_positions)


if __name__ == "__main__":

    import matplotlib.pyplot as plt

    data = load_input()
    
    positions = []
    n_knots = []
    for knots in range(2, 400):
        print(f"Running simulation for {knots = }")
        grid = RopeGrid(n_knots=knots)
        unique_tail_positions = grid.simulate(data)
        positions.append(unique_tail_positions)
        n_knots.append(knots)

        if unique_tail_positions == 1:
            print(f"Tail does not move at {knots} knots.")
            break
    

    plt.scatter(x=n_knots, y=positions)
    plt.show()  
