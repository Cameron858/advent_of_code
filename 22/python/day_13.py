def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_13_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines
  

def check_order(v1, v2) -> bool:
    print(f"Comparing {v1=} and {v2=}")

    if isinstance(v1, list) and isinstance(v2, list):
        for v1_1, v2_1 in zip(v1, v2):
            result = check_order(v1_1, v2_1)
            print(f"{result = }")
            if result:
                print(f"Inputs {v1_1} and {v2_1} are correctly ordered.")
                return True
        
        print(f"Ran out of list items.")
        if len(v1) < len(v2):
            print(f"Left side ran out of inputs. Returning True")
            return True
        elif len(v1) > len(v2):
            print("Right side ran out of items. Returning False")
            return False
    
    if isinstance(v1, int) and isinstance(v2, int):
        print("Both are int")
        if v1 < v2:
            print(f"v1 is less than v2")
            return True
        elif v1 > v2:
            print(f"v1 is bigger than v2")
            return False
        else:
            pass
    
    if (isinstance(v1, list) and isinstance(v2, int)):
        for v1_1 in v1:
            if check_order(v1_1, v2):
                return True
            else:
                continue
    
    if (isinstance(v1, int) and isinstance(v2, list)):
        for v2_1 in v2:
            if check_order(v1, v2_1):
                return True
            else:
                continue


def part_1(data: list[str]):

    pairs = []
    correctly_ordered_pairs = 0

    # parse data
    index = 0
    while index < len(data) - 1:
        chunk = data[index:index + 2]
        chunk = [eval(p.strip()) for p in chunk]
        pairs.append(chunk)       
        
        index += 3

    for index, pair in enumerate(pairs):
        
        if check_order(pair[0], pair[1]):
            print(f"Pair {index + 1} is correctly ordered.\n")
            correctly_ordered_pairs += index + 1
        else:
            print(f"Pair {index + 1} is not ordered.\n")
    
    print(f"{correctly_ordered_pairs=}")


if __name__ == "__main__":
    data = load_input()
    part_1(data)