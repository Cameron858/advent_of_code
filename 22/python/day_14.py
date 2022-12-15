from copy import deepcopy
import math


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_14.txt") as file_input:
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
    scan[0][sand_source_column - min_col] = '+'
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
    unit = 0
    while True:
        print("Spawning sand...", unit)

        initial_position = (sand_source_column, 1)
        x, y = initial_position
        x -= min_col

        try:
            moving = True
            while moving:
    
                temp_scan = deepcopy(scan)
                temp_scan[y][x] = 'O'
                display_scan(temp_scan)

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


def find_pyramid_base_width(height: int):
    # 1 -> 1
    # 2 -> 3
    # 3 -> 5
    # 4 -> 7
    return 2 * (height) - 1


def part_2(data):

    sand_source_column = 500
    data: list[list[tuple[int, int]]] = [[(int(d.split(",")[0]), int(d.split(",")[1])) for d in row.strip().split(" -> ")] for row in data]

    column_numbers = []
    row_numbers = []
    for row in data:
        for point in row:
            column_numbers.append(point[0])
            row_numbers.append(point[1])
    
    min_col, max_col = min(column_numbers), max(column_numbers)
    min_row, max_row = min(row_numbers), max(row_numbers)
    print(f"Column range: {min_col} to {max_col}\nRow range: {min_row} to {max_row}")
    print(f"The scan has {max_row + 1} rows and {max_col - min_col + 1} columns")
    inf_floor_width = find_pyramid_base_width(max_row + 2)
    print(f"The inf floor must be {inf_floor_width} wide")
    print(f"{(inf_floor_width - 1) // 2} must be added either side of the sand source.")

    # padding for inf floor
    l_dist = sand_source_column - min_col
    r_dist = (max_col - min_col) - l_dist
    print(f"The source is {l_dist} away from the left and {r_dist} away from the right")
    left_padding = ((inf_floor_width - 1) // 2) - l_dist
    right_padding =  ((inf_floor_width - 1) // 2) - r_dist + 1
    print(f"{left_padding=}, {right_padding=}")

    # create empty scan
    scan = [['.' for _ in range(max_col - min_col + 1)] for _ in range(max_row + 1)]  
    
    # draw on rocks
    rock_positions_list = set()
    scan[0][sand_source_column - min_col] = '+'
    for row in data:
        for p1, p2 in swindow(row):
            rock_positions = interpolate_between_two_points(p1, p2)
            for rp in rock_positions:
                x, y = rp
                # print(f"Drawing {x=} and {y=} @ x={x - min(column_numbers)} and y={y}")
                rock_positions_list.add((y, x - min_col))
                scan[y][x - min_col] = '#'

    # add inf floor to scan
    scan = [['.' for _ in range(left_padding)] + row + ['.' for _ in range(right_padding)] for row in scan]
    scan.append(['.' for _ in range(len(scan[0]))])
    scan.append(['#' for _ in range(len(scan[0]))])
    # display_scan(scan)

    # simulate sand
    unit = 0
    while scan[0][(sand_source_column - min_col) + left_padding] not in ['#', 'O']:
        initial_position = (sand_source_column  + left_padding, 0)
        x, y = initial_position
        x -= min_col

        try:
            moving = True
            while moving:
                # temp_scan = deepcopy(scan)
                # temp_scan[y][x] = 'O'
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
    part_2(data)
