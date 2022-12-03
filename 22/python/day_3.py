def load_input():
    """Load in the data for Day 1."""
    try:
        with open(r"22\data\day_3.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def part_1():
    input_lines = load_input()
    
    sum = 0
    for id, rucksack in enumerate(input_lines):
        rucksack = rucksack.strip()

        print(rucksack)
        size = len(rucksack) // 2
        comp1, comp2 = rucksack[0:size], rucksack[size:]
        
        for item in comp1:
            if item in comp2:
                print(f"Found {item} shared")
                
                if item.islower():
                    sum += ord(item) - 96 
                else:
                    sum += ord(item.lower()) - 96 + 26
                
                break
    
    print(sum)


def part_2():
    input_lines = load_input()

    sum = 0
    index = 0
    while index < (len(input_lines) - 2):
        group = input_lines[index:index + 3]
        r1, r2, r3 = group[0], group[1], group[2]

        for item in r1:
            if item in r2 and item in r3:
                print(f"Shared {item}")
                if item.islower():
                    sum += ord(item) - 96 
                else:
                    sum += ord(item.lower()) - 96 + 26
                
                break

        index += 3
    
    print(sum)



if __name__ == "__main__":
    part_2()
    