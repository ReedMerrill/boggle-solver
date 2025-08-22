import random
from typing import List
import pprint

dice = [
    ["R", "I", "F", "O", "B", "X"],
    ["I", "F", "E", "H", "E", "Y"],
    ["D", "E", "N", "O", "W", "S"],
    ["U", "T", "O", "K", "N", "D"],
    ["H", "M", "S", "R", "A", "O"],
    ["L", "U", "P", "E", "T", "S"],
    ["A", "C", "I", "T", "O", "A"],
    ["Y", "L", "G", "K", "U", "E"],
    ["Qu", "B", "M", "J", "O", "A"],
    ["E", "H", "I", "S", "P", "N"],
    ["V", "E", "T", "I", "G", "N"],
    ["B", "A", "L", "I", "Y", "T"],
    ["E", "Z", "A", "V", "N", "D"],
    ["R", "A", "L", "E", "S", "C"],
    ["U", "W", "I", "L", "R", "G"],
    ["P", "A", "C", "E", "M", "D"],
]


def make_grid(size: int = 4, dice: List[List[str]] = dice) -> List[List[str]]:
    # shuffle the order of the dice
    random.shuffle(dice)
    # roll each die and store the result in a list
    random_letters = [random.choice(die) for die in dice]
    # split list of strings into a grid (list of lists)
    grid = []
    for i in range(size):
        row_start = i * size
        row_end = row_start + size
        row = random_letters[row_start:row_end]
        grid.append(row)
    return grid


def check_trie():
    pass


# TODO: add lexicon param
def search_grid(grid: List[List[str]], row_i, col_j):
    """Does a Depth First Search starting from an element of a grid"""

    size = len(grid)

    directions = [[-1, 0], [-1, 1], [-1, -1], [0, 1], [0, -1], [1, 0], [1, 1], [1, -1]]

    visited = []
    stack = []

    visited.append([row_i, col_j])
    stack.append([row_i, col_j])

    print("===============================================")
    print(f"Starting Cell: {grid[stack[0][0]][stack[0][1]]} ({stack[0]})")

    while stack:

        print(f"stack: {stack}")
        print(f"visited: {visited}")
        s = stack.pop()

        for di, dj in directions:

            # potential coordinate of the next letter in the search
            next = [s[0] + di, s[1] + dj]

            # if next falls within the grid, add it to stack and visited
            if (
                (next[0] >= 0 and next[0] <= size - 1)
                and (next[1] >= 0 and next[1] <= size - 1)
                and (next not in visited)
            ):
                stack.append(next)
                visited.append(next)
                print(f"letter: {grid[next[0]][next[1]]}")


# TODO: add lexicon param
def traverse_grid(grid: List[List[str]]):

    # begin the search from every letter in the grid
    for row_i, row in enumerate(grid):
        for col_j, _ in enumerate(row):
            search_grid(grid, row_i, col_j)


def main():
    grid = make_grid()
    # TEST:
    grid = [["t", "o", "n"], ["e", "w", "l"], ["a", "b", "r"]]
    pprint.pp(grid)
    traverse_grid(grid=grid)


if __name__ == "__main__":
    main()
