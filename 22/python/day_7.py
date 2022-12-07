from enum import Enum, auto


class LineItemType(Enum):
    Command = auto()
    Directory = auto()
    ChildItem = auto()


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_7_example.txt") as file_input:
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
    
    print(file_tree)

    print("Calculate sizes")

    d = {}
    total_sizes, d = get_size('/', file_tree, d)
    print(d)


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

    print(base_dir, size, d)
    return size, d
                

if __name__ == "__main__":
    input_ = load_input()
    part_1(input_)
