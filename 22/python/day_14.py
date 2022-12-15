from copy import deepcopy


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_14_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def display_scan(scan: list[list[str]]):
    print("")
    for row in scan:
        print("".join(row))


def swindow(data: list, size=2):
    index = 0
    while index < len(data) - 1:
        s = data[index:index + 2]
        yield s[0], s[1]
        index += 1


def interpolate_between_two_points(p1: tuple[int, int], p2: tuple[int, int]):
    """
    498,4 -> 498,6 = [(498, 4), (498, 5), (498, 6)]
    498,6 -> 496,6 = [(498, 6), (497, 6), (496, 6)]
    """
    points = []
    # same x
    if p1[0] == p2[0]:
        low, high = min([p1[1], p2[1]]), max([p1[1], p2[1]])
        for y in range(low, high + 1):
            points.append((p1[0], y))
        
    # same y
    if p1[1] == p2[1]:
        low, high = min([p1[0], p2[0]]), max([p1[0], p2[0]])
        for x in range(low, high + 1):
            points.append((x, p1[1]))
    
    return points


def part_1(data: list[str]):
    
    sand_source_column = 500
    data: list[list[tuple[int, int]]] = [[(int(d.split(",")[0]), int(d.split(",")[1])) for d in row.strip().split(" -> ")] for row in data]
    print(data[0])

    column_numbers = []
    row_numbers = []
    for row in data:
        for point in row:
            column_numbers.append(point[0])
            row_numbers.append(point[1])
    
    min_col, max_col = min(column_numbers), max(column_numbers)
    min_row, max_row = min(row_numbers), max(row_numbers)
    print(f"Column range: {min_col} to {max_col}\nRow range: {min_row} to {max_row}")

    # create empty scan
    scan = [['.' for _ in range(max_col - min_col + 1)] for _ in range(max_row + 1)]
    print(f"The scan has {max_row + 1} rows and {max_col - min_col + 1} columns")
    
    # draw on rocks
    rock_positions_list = set()
    scan[0][500 - min_col] = '+'
    for row in data:
        for p1, p2 in swindow(row):
            rock_positions = interpolate_between_two_points(p1, p2)
            for rp in rock_positions:
                x, y = rp
                # print(f"Drawing {x=} and {y=} @ x={x - min(column_numbers)} and y={y}")
                rock_positions_list.add((y, x - min_col))
                scan[y][x - min_col] = '#'

    display_scan(scan)

    # simulate sand
    fallen_sand_positions = set()
    unit = 0
    while True:
        print("Spawning sand...", unit)

        initial_position = (500, 1)
        x, y = initial_position
        x -= min_col

        try:
            moving = True
            while moving:
    
                temp_scan = deepcopy(scan)
                temp_scan[y][x] = 'O'
                # display_scan(temp_scan)

                if scan[y + 1][x] not in ['#', 'O']:
                    # print(f"Moving down.")
                    y += 1
                else:
                    # print("The path below is blocked. Check diagonals")
                    # bottom left
                    if scan[y + 1][x - 1] not in ['#', 'O']:
                        # print("Bottom left is free.")
                        y += 1
                        x -= 1
                        continue
                    
                    if scan[y + 1][x + 1] not in ['#', 'O']:
                        y += 1
                        x += 1
                        # print("Bottom right is free")
                        continue
                    
                    # print(f"This unit cannot move.")
                    scan[y][x] = 'O'
                    # fallen_sand_positions.add((x, y))
                    moving = False
        except IndexError:
            print(f"Unit {unit} has fallen into the abyss!")
            break
        
        unit += 1
    
    print(f"{unit} units of sand fell.")


if __name__ == "__main__":
    data = load_input()
    part_1(data)