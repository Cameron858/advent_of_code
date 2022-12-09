

def load_input():
    """Load in the data."""
    try:
        with open(r"21\data\day_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines



def sliding_window(win_size: int, data: list[int]):
    max_index = len(data)

    index = 0
    while index < (max_index - win_size + 1):
        yield data[index:index + win_size]
        index += 1


def part_1(input_data):
    print(input_data)


def part_2(input_data):

    input_data = [int(measurement.strip()) for measurement in input_data]
    
    window_sums = []
    for window in sliding_window(3, input_data):
        window_sums.append(sum(window))
    
    increases = 0
    for window in sliding_window(2, window_sums):
        if window[1] > window[0]:
            increases += 1

    print(increases)


if __name__ == "__main__":
    input_data = load_input()
    part_2(input_data)