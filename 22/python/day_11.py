def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_11.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


class Item: 

    def __init__(self, worry_level) -> None:
        self.worry_level: int = worry_level


class Monkey:

    monkeys = []

    def __init__(self, monkey_id: int, starting_items: list[int], operator: str, operation_value: int | str,
    test_value: int, test_true_monkey: int, test_false_monkey: int) -> None:
        self.id = monkey_id
        self.starting_items = starting_items
        self.operator: str = operator
        self.operation_value: int = operation_value
        self.test_value: int = test_value
        self.test_true_monkey: int = test_true_monkey
        self.test_false_monkey: int = test_false_monkey

    def __repr__(self) -> str:
        return f"{self.__dict__}"


def part_1(data: list[str]):

    print(data)

    monkeys: list[Monkey] = []

    # parse data
    for line in data:

        if line.startswith("Monkey"):
            monkey_id = int(line.split(" ")[1][:-1])
            print(f"{monkey_id=}")
        
        if line.startswith("Starting items"):
            starting_items = line.split(" ")[2:]
            starting_items = [int(item.replace(',', '')) for item in starting_items]
            print(f"{starting_items=}")
        
        if line.startswith("Operation"):
            splits = line.split(" ")
            operator = splits[-2]

            try:
                operator_value = int(splits[-1])
            except ValueError:
                operator_value = splits[-1]

            print(f"{operator=}, {operator_value=}")
        
        if line.startswith("Test"):
            splits = line.split(" ")
            test_value = int(splits[-1])
            print(f"{test_value=}")
        
        if line.startswith("If true"):
            splits = line.split(" ")
            test_true_monkey = int(splits[-1])
            print(f"{test_true_monkey=}")

        if line.startswith("If false"):
            splits = line.split(" ")
            test_false_monkey = int(splits[-1])
            print(f"{test_false_monkey=}")

        try:
            monkey = Monkey(monkey_id, starting_items, operator, operator_value, test_value,
                        test_true_monkey, test_false_monkey)
            monkeys.append(monkey)
        except UnboundLocalError:
            pass
        
    print(monkeys)
    
    # simulate
    # for round in range(20):
    #     print(f"Starting round {round + 1}")


if __name__ == "__main__":
    data = load_input()
    part_1(data)