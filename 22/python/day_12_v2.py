import string
import math


def load_input():
    """Load in the data."""
    try:
        with open(r"22\data\day_12.txt") as file_input:
            input_lines = file_input.readlines()
    except OSError as e:
        print(f"Error {e} raised.")
        exit()

    return input_lines
    
def find_start_and_end_pos(heights: list[list[str]]):
    start = None
    end = None
    for ri, r in enumerate(heights):
        for ci, char in enumerate(r):
            if char == "S":
                start = (ri, ci)
            if char == "E":
                end = (ri, ci)
    
    return start, end


def create_char_map() -> dict[str, list[str]]:
    character_moves = {}
    # map possible positons for each letter
    letters = string.ascii_lowercase
    for index, char in enumerate(letters[0:-1]):
        if index == 0:
            character_moves[char] = [char, letters[index + 1]]
        else:
            character_moves[char] = [letters[index - 1], char, letters[index + 1]]
    # add end position to possible move list
    character_moves["z"] = ['y', 'z']

    return character_moves

class Node:

    def __init__(self, pos, char: str) -> None:
        
        self.pos = pos
        self.parent = None
        self.char = char
        self.get_valid_chars()
        
        self.g = 0
        self.h = 0
        self.f = 0

    def __repr__(self) -> str:
        return f"Node({self.pos}, char={self.char}, , valid_chars={self.valid_chars}, g={self.g}, h={self.h}, f={self.f})"

    def get_valid_chars(self):
        cm = create_char_map()
        self.valid_chars = cm[self.char]


class AStar:

    def __init__(self, maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> None:

        self.maze = maze
        self.start_position = start
        self.end_position = end

        self.closed_nodes: list[Node] = []
        self.open_nodes: list[Node] = []
        self.path = []
    
    def pathfind(self):
        
        self.open_nodes.append(Node(pos=self.start_position, char="a"))

        while self.open_nodes:

            # get the node with the least f value from the open list
            self.open_nodes = sorted(self.open_nodes, key=lambda node: node.f)
            current_node = self.open_nodes[0]
            self.open_nodes = self.open_nodes[1:]
            
            print(f"The current node is {current_node}")
            self.closed_nodes.append(current_node.pos)

            if current_node.pos == self.end_position:
                print(f"The end has been found")

                path = []
                current = current_node
                while current is not None:
                    path.append(current.pos)
                    current = current.parent
                
                return path[::-1]
            
            # get adjacent nodes
            children = self.get_cardinal_adjacents(node=current_node)

            for child in children:

                child.parent = current_node

                if child.pos in self.closed_nodes:
                    # print(f"{child} has already been visited")
                    continue
                
                # current_node g + distance from child to current
                child.g = current_node.g + 1
                # distance from child to end
                child.h = int(math.dist(child.pos, self.end_position))
                # child.h = abs(child.pos[0] - self.end_position[0]) + abs(child.pos[1] - self.end_position[1])
                child.f = child.g + child.h              

                for open_node in self.open_nodes:
                    if open_node.pos == child.pos and child.g > open_node.g:
                        continue

                # print(f"Add {child} to open node.")
                self.open_nodes.append(child)


    def _pop_lowest_f_node_from_open_list(self) -> Node:
        
        # arbitarily set the lowest f to the f value of the first node
        lowest_f_cost = self.open_nodes[0].f
        lowest_f_index = 0
        for index, node in enumerate(self.open_nodes):
            if node.f < lowest_f_cost:
                lowest_f_cost = node.f
                lowest_f_index = index
        
        lowest_f_node = self.open_nodes.pop(lowest_f_index)
        # print(f"Returning lowest f node {lowest_f_node}")
        return lowest_f_node
    
    def get_cardinal_adjacents(self, node: Node) -> list[Node]:
        """
        (1, 1) -> [(0, 1), (2, 1), (1, 0), (2, 0)]
        """
        row, col, = node.pos
        cardinal_adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        
        valid_positions = []
        for temp_pos in cardinal_adjacent_positions:

            if (0 <= temp_pos[0] < len(self.maze)) and (0 <= temp_pos[1] < len(self.maze[1])):
                maze_char =  self.maze[temp_pos[0]][temp_pos[1]]

                if maze_char in node.valid_chars:
                    new_node = Node(pos=temp_pos, char=maze_char)
                    valid_positions.append(new_node)
        
        return valid_positions


if __name__ == "__main__":
    # p1 > 117
    # 200 -> error
    # 250 -> error
    data = load_input()
    data = [[c for c in row.strip()] for row in data]
    
    start, end = find_start_and_end_pos(data)
    print(f"{start=}, {end=}")

    data[start[0]][start[1]] = "a"
    data[end[0]][end[1]] = "z"

    algo = AStar(data, start, end)
    path = algo.pathfind()
    print(path, len(path))
