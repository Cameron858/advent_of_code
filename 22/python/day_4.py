def load_input():
    """Load in the data for Day 1."""
    try:
        with open(r"22\data\day_4.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def part_1():
    input_lines = load_input()  
    print(input_lines)

    count = 0
    for pair in input_lines:
        sections = pair.split(",")
        print(sections)
        s1, s2 = sections[0], sections[1]
        s1 = s1.split("-")
        s2 = s2.split("-")

        s1_1 = int(s1[0])
        s1_2 = int(s1[1])
        s2_1 = int(s2[0])
        s2_2 = int(s2[1])

        if (s1_1 >= s2_1) and (s1_2 <= s2_2):
            print("First fits into second")
            count += 1
        elif (s2_1 >= s1_1) and (s2_2 <= s1_2):
            print("Second fits into first.")
            count += 1
    
    print(count)


def part_2():
    input_lines = load_input()
    print(input_lines)
    test = ['6-67, 68-68', '2-4, 6-8', '2-3, 4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8', '95-95, 12-86', '90-93, 1-88', '90-93,1-88']
    # input_lines = test
    count = 0
    for pair in input_lines:
        sections = pair.split(",")
        print(sections)
        s1, s2 = sections[0], sections[1]
        s1 = s1.split("-")
        s2 = s2.split("-")

        s1_1 = int(s1[0])
        s1_2 = int(s1[1])
        s2_1 = int(s2[0])
        s2_2 = int(s2[1])

        if (s1_2 >= s2_1) and (s1_1 <= s2_1):
            print("Overlap 1")
            count += 1
        elif (s2_1 <= s1_1) and (s2_2 >= s1_1):
            print("Overlap 2")
            count += 1

    print(count)


if __name__ == "__main__":
    part_2()