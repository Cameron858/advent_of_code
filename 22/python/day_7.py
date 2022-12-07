from enum import Enum, auto


class LineItemType(Enum):
    Command = auto()
    Directory = auto()
    ChildItem = auto()


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_7.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def get_dir_children(input_lines: list[str], index):

    children = []
    for item in input_lines[index + 2:]:

        if item.startswith("$"):
            break
        else:
            children.append(item)
    
    return children


def part_1(input_lines: list[str]):
    
    max_drive_space = 70_000_000
    space_needed = 30_000_000

    file_tree: dict[list[str]] = {}
    file_path = []
    for index, line in enumerate(input_lines):
        
        parts = line.split(" ")
        if parts[0] == "$":
            line_item_type = LineItemType.Command
        elif parts[0] == "dir":
            line_item_type = LineItemType.Directory
        else:
            line_item_type = LineItemType.ChildItem
        

        if line_item_type == LineItemType.Command:
            
            if parts[1] == "cd" and parts[2] != "..":
                cwd = parts[2]
                file_path.append(cwd)
                # print("-".join(file_path))
                children = get_dir_children(input_lines, index)
                # print(children)
                file_tree["-".join(file_path)] = children
            elif parts[1] == "cd" and parts[2] == "..":
                file_path.pop(-1)
    
    print("Calculate sizes")
    d = {}
    total_sizes, d = get_size('/', file_tree, d)
    print(d)

    part_1_sum = 0
    for k, v in d.items():
        if v < 100000:
            part_1_sum += v

    print("Part 1: ", part_1_sum)

    return d

def get_size(base_dir: str, file_tree: dict[list[str]], d):
    
    size = 0
    for children in file_tree[base_dir]:

        if not children.startswith("dir"):
            size += int(children.split(" ")[0])
            # print(f"Found child {children.split()[1]} of size {children.split()[0]}")
        elif children.startswith("dir"):
            new_dir = children.split(" ")[1]
            new_base_dir = "-".join([base_dir, new_dir])

            new_size, new_dict = get_size(new_base_dir, file_tree, d)
            size += new_size

    d[base_dir] = size
    
    try:
        d = {**d, **new_dict}
    except UnboundLocalError:
        pass

    return size, d
                

def part_2(part_1_solution: dict):
    max_drive_space = 70_000_000
    space_needed = 30_000_000
    print(f"{max_drive_space = }")
    current_used_space = max(part_1_solution.values())
    print(f"Currently using: {current_used_space}")
    print(f"Space needed: {space_needed}")
    left_over_space = max_drive_space - current_used_space
    print(f"{left_over_space = }")
    space_difference = space_needed - left_over_space
    print(f"{space_difference = }")

    possible_dirs = []
    for k, v in part_1_solution.items():

        if v > space_difference:
            possible_dirs.append(v)
    
    print(possible_dirs)
    print(min(possible_dirs))


if __name__ == "__main__":
    input_ = load_input()
    part_1_dict = part_1(input_)
    part_2(part_1_dict)
