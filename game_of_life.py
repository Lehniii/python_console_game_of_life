import random
import time
import os
import sys

# Function to initialize a random grid
def random_grid(width, height):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

# Function to print the grid to the console
def print_grid(grid):
    os.system("cls" if os.name == "nt" else "clear")  # Clear the console
    for row in grid:
        print("".join(["■" if cell else " " for cell in row]))
    print("\n")

# Function to update the grid based on the rules of the Game of Life
def update_grid(grid):
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = [
                grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][(j + 1) % len(grid[0])],
                grid[i][j - 1], grid[i][(j + 1) % len(grid[0])],
                grid[(i + 1) % len(grid)][j - 1], grid[(i + 1) % len(grid)][j], grid[(i + 1) % len(grid)][(j + 1) % len(grid[0])]
            ]

            live_neighbors = sum(neighbors)
            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid

# Main function to run the game
def main(width, height, generations, delay):
    grid = random_grid(width, height)

    for _ in range(generations):
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 8 or args[0] != "-width" or args[2] != "-height" or args[4] != "-generations" or args[6] != "-delay":
        print("Usage: python game_of_life.py -width <width> -height <height> -generations <generations> -delay <delay>")
    else:
        width = int(args[1])
        height = int(args[3])
        generations = int(args[5])
        delay = float(args[7])
        main(width, height, generations, delay)
