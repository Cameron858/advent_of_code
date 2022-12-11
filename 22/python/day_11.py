def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_11_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return [l.strip() for l in input_lines]


class Item: 

    def __init__(self, worry_level) -> None:
        self.worry_level: int = worry_level
    
    def new_worry_level(self, operator: str, operator_value: int | str):
        print(f"Calculating new worry level {operator=}, {operator_value=}")

        if isinstance(operator_value, int):
            if operator == "*":
                self.worry_level *= operator_value
            elif operator == "+":
                self.worry_level += operator_value
            elif operator == "-":
                self.worry_level -= operator_value
            elif operator == "/":
                self.worry_level /= operator_value
        
        if operator_value == "old":
            self.worry_level *= self.worry_level
        
        print(f"New worry level is {self.worry_level}")
    
    def divide_worry_level(self):
        self.worry_level = self.worry_level // 3
        print(f"After dividing my new worry level is {self.worry_level}")
    
    def __repr__(self) -> str:
        return f"{self.worry_level}"


class Monkey:

    monkeys: list['Monkey'] = []

    def __init__(self, monkey_id: int, starting_items: list[Item], operator: str, operation_value: int | str,
    test_value: int, test_true_monkey: int, test_false_monkey: int) -> None:
        self.id: int = monkey_id
        self.items: list[Item] = starting_items
        self.operator: str = operator
        self.operation_value: int = operation_value
        self.test_value: int = test_value
        self.test_true_monkey: int = test_true_monkey
        self.test_false_monkey: int = test_false_monkey
        self.total_items_inspected = 0

        Monkey.monkeys.append(self)

    def inspect_items(self):

        throw_list = []
        if self.items:
            for idx, item in enumerate(self.items):
                self.total_items_inspected += 1

                print(f"Inspecting item {item}")
                item.new_worry_level(self.operator, self.operation_value)
                item.divide_worry_level()

                if item.worry_level % self.test_value == 0:
                    print(f"Test passed, throwing to monkey {self.test_true_monkey}")
                    throw_list.append((idx, self.test_true_monkey))
                else:
                    print(f"Test failed, throwing to monkey {self.test_false_monkey}")
                    throw_list.append((idx, self.test_false_monkey))
        
        for _, monkey_id in throw_list:
            item = self.items.pop(0)
            m = Monkey.get_monkey_by_id(monkey_id)
            m.items.append(item)


    def __repr__(self) -> str:
        return f"{self.__dict__}"
    
    @classmethod
    def get_monkey_by_id(cls, id: int):
        m = [m for m in cls.monkeys if m.id == id]

        if m:
            return m[0]
        else:
            raise ValueError(f"No monkey found for {id=}")
    
    @classmethod
    def print_monkey_inspections(cls):

        inspections = []
        for monkey in Monkey.monkeys:
            print(f"Monkey {monkey.id} inspected items {monkey.total_items_inspected} times")
            inspections.append(monkey.total_items_inspected)
        
        return inspections


def part_1(data: list[str]):

    monkeys: list[Monkey] = []

    # parse data
    idx = 0
    while idx < len(data):
        monkey_chunk = data[idx:idx + 6]
        print(monkey_chunk)

        for line in monkey_chunk:

            if line.startswith("Monkey"):
                monkey_id = int(line.split(" ")[1][:-1])
                print(f"{monkey_id=}")
            
            if line.startswith("Starting items"):
                starting_items = line.split(" ")[2:]
                starting_items = [int(item.replace(',', '')) for item in starting_items]
                starting_items = [Item(worry_level=v) for v in starting_items]
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
        
        monkey = Monkey(monkey_id, starting_items, operator, operator_value, test_value,
                    test_true_monkey, test_false_monkey)

        idx += 7
    
    print(Monkey.monkeys)

    for round in range(20):
        print(f"Starting round {round}")
        for m in Monkey.monkeys:
            print(m.id)
            m.inspect_items()
        
        inspections = Monkey.print_monkey_inspections()
    
    print(inspections)
    inspections = sorted(inspections, reverse=True)[0:2] 
    print(inspections)
    print(inspections[0] * inspections[1])



if __name__ == "__main__":
    data = load_input()
    part_1(data)