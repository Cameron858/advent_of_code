import re


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_15_example_1.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines


def sensor_beacon_distance(sensor: tuple[int, int], beacon: tuple[int, int]) -> int:
    assert isinstance(beacon, tuple)

    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


class Sensor:

    def __init__(self, pos) -> None:
        self.position = pos
        self.closest_beacon_position = None
        self.distance_to_closest_beacon = None
    
    def __repr__(self) -> str:
        return f"Sensor({self.position}, {self.closest_beacon_position}, {self.distance_to_closest_beacon})"


def draw(sensors: Sensor):
    pass


def part_1(data: list[str]):
    
    # find and convert to int all numbers in string
    data = [[i for i in map(int, re.findall(r"[+-]?\d+", row.strip()))] for row in data]
    print(data)

    sensors: list[Sensor] = []
    beacons = set()
    for row in data:
        sensors.append(Sensor((row[0], row[1])))
        beacons.add((row[2], row[3]))

    print(f"{sensors=}\n{beacons=}\n")

    for sensor in sensors:
        distances = []
        for beacon in beacons:
            d = sensor_beacon_distance(sensor.position, beacon)
            distances.append((beacon, d))
        closest_beacon = sorted(distances, key=lambda x: x[1])[0][0]
        distance_to_beacon = sorted(distances, key=lambda x: x[1])[0][1]
        sensor.closest_beacon_position = closest_beacon
        sensor.distance_to_closest_beacon = distance_to_beacon

    print(sensors)
    draw(sensors)

    
if __name__ == "__main__":
    data = load_input()
    part_1(data)