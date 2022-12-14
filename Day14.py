# Parse the input and generate the locations of the stone
def generate_moves(current, next):
    current_column, current_row = current.split(",")
    next_column, next_row = next.split(",")
    current_column = int(current_column)
    current_row = int(current_row)
    next_column = int(next_column)
    next_row = int(next_row)
    stones = set()
    stones.add((current_row, current_column))
    while current_column != next_column or current_row != next_row:
        if current_column < next_column:
            current_column += 1
        elif current_column > next_column:
            current_column -= 1
        elif current_row < next_row:
            current_row += 1
        elif current_row > next_row:
            current_row -= 1
        stones.add((current_row, current_column))
    return stones


# Simulate the falling of sand
def simulate_sand(grid):
    sand_row = 0
    sand_column = 500
    while True:
        # Check if the sand fell out of the map
        if sand_column == 0 or sand_column >= len(grid[0]) - 1 or sand_row >= len(grid) - 1:
            return (grid, True)
        elif grid[sand_row + 1][sand_column] == 0:
            sand_row += 1
        elif grid[sand_row + 1][sand_column - 1] == 0:
            sand_row += 1
            sand_column -= 1
        elif grid[sand_row + 1][sand_column + 1] == 0:
            sand_row += 1
            sand_column += 1
        else:
            grid[sand_row][sand_column] = 1
            return (grid, False)


# Simulate the falling of sand
def simulate_sand_until_blocked(grid):
    sand_row = 0
    sand_column = 500

    # If the source of the sand is blocked
    if grid[sand_row][sand_column] == 1:
        return (grid, True)

    while True:
        if grid[sand_row + 1][sand_column] == 0:
            sand_row += 1
        elif grid[sand_row + 1][sand_column - 1] == 0:
            sand_row += 1
            sand_column -= 1
        elif grid[sand_row + 1][sand_column + 1] == 0:
            sand_row += 1
            sand_column += 1
        else:
            grid[sand_row][sand_column] = 1
            return (grid, False)

# Read the inputs from a .txt file
lines = None
with open("Day14.txt", "r") as file:
    lines = file.readlines()

# Contain the location of all the stones
stone_location = set()

# Iterate over the input to find the location of all the stones in the map
for line in lines:
    structures = line.split("->")
    for i in range(0, len(structures) - 1):
        stones = generate_moves(structures[i], structures[i + 1])
        for stone in stones:
            stone_location.add(stone)

# Iterate over the stone locations to find the maximum size of the map
max_row = 0
max_column = 0
for stone in stone_location:
    max_row = max(max_row, stone[0])
    max_column = max(max_column, stone[1])

# Create a grid
grid = []
for i in range(max_row + 2):
    grid.append([0] * (max_column + 2))

for stone in stone_location:
    grid[stone[0]][stone[1]] = 1
 
sand_came_to_rest = 0
while True:
    grid, sand_fell_off_map = simulate_sand(grid)
    if sand_fell_off_map:
        break
    sand_came_to_rest += 1

# Answer to part 1
print(sand_came_to_rest)

# Create a grid
grid = []
for i in range(max_row + 2):
    grid.append([0] * (max_column + 200))
grid.append([1] * (max_column + 200))

for stone in stone_location:
    grid[stone[0]][stone[1]] = 1

sand_came_to_rest = 0
while True:
    grid, source_blocked = simulate_sand_until_blocked(grid)
    if source_blocked:
        break
    sand_came_to_rest += 1

# Answer to part 2
print(sand_came_to_rest)