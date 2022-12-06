def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_6.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


def unique(string):

    char_list = []
    for char in string:

        if char not in char_list:
            char_list.append(char)
        else:
            return False
    
    print(f"Unique string found: {string}")
    return True

def first_unique_n_chars():
    
    n_length = 4
    input_buffer: str = load_input()[0]
    print(input_buffer[0:-n_length])

    index = 0  
    while index < (len(input_buffer) - n_length):
        slice = input_buffer[index:index + n_length]

        if unique(slice):
            print("First unique @ ", index + n_length)
            break
        
        index += 1


if __name__ == "__main__":
    first_unique_n_chars()