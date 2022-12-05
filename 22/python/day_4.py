def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_4.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def get_section_limits(pair):
    sections = pair.split(",")
    print(sections)
    s1, s2 = sections[0], sections[1]
    s1 = s1.split("-")
    s2 = s2.split("-")

    s1_1 = int(s1[0])
    s1_2 = int(s1[1])
    s2_1 = int(s2[0])
    s2_2 = int(s2[1])

    return s1_1, s1_2, s2_1, s2_2


def part_1():
    input_lines = load_input()  
    print(input_lines)

    complete_intersect_count = 0
    for pair in input_lines:
        s1_1, s1_2, s2_1, s2_2 = get_section_limits(pair)

        if (s1_1 >= s2_1) and (s1_2 <= s2_2):
            print("First fits into second")
            complete_intersect_count += 1
        elif (s2_1 >= s1_1) and (s2_2 <= s1_2):
            print("Second fits into first.")
            complete_intersect_count += 1
    
    print(complete_intersect_count)


def part_2():
    input_lines = load_input()
    print(input_lines)
    overlap_count = 0
    for pair in input_lines:
        s1_1, s1_2, s2_1, s2_2 = get_section_limits(pair)

        if (s1_2 >= s2_1) and (s1_1 <= s2_1):
            print("Overlap 1")
            overlap_count += 1
        elif (s2_1 <= s1_1) and (s2_2 >= s1_1):
            print("Overlap 2")
            overlap_count += 1

    print(overlap_count)


if __name__ == "__main__":
    part_2()