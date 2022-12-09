from collections import Counter


def load_input():
    """Load in the data."""
    try:
        with open(r"21\data\day_3.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def display(data):
    for d in data:
        print(d)


def count_most_common_in_position(position: int, data: list[str]):
    
    pos_list = []
    for row in data:
        pos_list.append(row[position])
    
    c = Counter(pos_list)

    return c.most_common(1)[0][0]


def part_1(input_data: list[str]):
    input_data = [num.strip() for num in input_data]
    display(input_data)
    
    gamma_rate = []
    for position, _ in enumerate(input_data[0]):
        c = count_most_common_in_position(position, input_data)
        gamma_rate.append(c)
    
    print(gamma_rate)

    epsilon_rate = []
    for char in gamma_rate:
        if char == "1":
            epsilon_rate.append("0")
        else:
            epsilon_rate.append("1")
    
    print(epsilon_rate)

    gamma_rate = "".join(gamma_rate)
    epsilon_rate = "".join(epsilon_rate)

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    print(gamma_rate * epsilon_rate)


def part_2(input_data):
    pass


if __name__ == "__main__":
    input_data = load_input()[0:5]
    part_1(input_data)