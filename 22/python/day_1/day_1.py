

def load_input():
    with open("day_1/22_01.txt") as file_input:
        lines = file_input.readlines()

    return lines


def aoc_1():

    lines = load_input()    

    elfs = []
    sum = 0
    for value in lines:
        if value == '\n':
            elfs.append(sum)
            sum = 0
        else:
            calories = int(value)
            sum += calories
    
    return elfs


def aoc_1_2():
    elfs = aoc_1()
    return sum(sorted(elfs, reverse=True)[0:3])


if __name__ == '__main__':

    max_elf = max(aoc_1())
    sum_top_three = aoc_1_2()
    print(f"{max_elf = }, {sum_top_three = }")