"""
Inputs:
    r, int - row value
    c, int - column value
    data, list(str) - a list of string values that form a 2D grid of numbers
    height, int - the height of the specified tree
Return:
    bool - indicates whether the tree at the specified row and column value is visible
"""
def is_visible(r, c, data, height):
    # If the tree is on the border of the grid, it is visible
    if r == 0 or c == 0 or r == len(data) - 1 or c == len(data[0]) - 1:
        return True

    # Initialize a list of bool that stores whether the tree is visible from above, below, left, and right on the grid
    visible = [True, True, True, True]

    # Check if the tree is not visible from above on the grid
    for i in range(0, r):
        if data[i][c] >= height:
            visible[0] = False
            break

    # Check if the tree is not visible from below on the grid
    for i in range(r + 1, len(data)):
        if data[i][c] >= height:
            visible[1] = False
            break

    # Check if the tree is not visible from the left on the grid
    for i in range(0, c):
        if data[r][i] >= height:
            visible[2] = False
            break

    # Check if the tree is not visible from the right on the grid
    for i in range(c + 1, len(data[0])):
        if data[r][i] >= height:
            visible[3] = False
            break
    
    if True in visible:
        return True
    else:
        return False

"""
Inputs:
    r, int - row value
    c, int - column value
    data, list(str) - a list of string values that form a 2D grid of numbers
    height, int - the height of the specified tree
Return:
    int - a scenic score for the specified tree   
"""
def compute_scenic_score(r, c, data, height):
    # If the tree is the border of the grid, it has a scenic score of 0
    if r == 0 or c == 0 or r == len(data) - 1 or c == len(data[0]) - 1:
        return 0

    # Initialize a list of int that stores the scenic score of the view from each direction
    scores = [0, 0, 0, 0]
    
    # Compute the scenic score for the view above the tree on the grid
    for i in range(r - 1, -1, -1):
        scores[0] += 1
        if data[i][c] >= height:
            break

    # Compute the scenic score for the view below the tree on the grid
    for i in range(r + 1, len(data)):
        scores[1] += 1
        if data[i][c] >= height:
            break

    # Compute the scenic score for the view to the left of the tree on the grid
    for i in range(c - 1, -1, -1):
        scores[2] += 1
        if data[r][i] >= height:
            break

    # Compute the scenic score for the view to the right of the tree on the grid
    for i in range(c + 1, len(data[0])):
        scores[3] += 1
        if data[r][i] >= height:
            break
    
    return scores[0] * scores[1] * scores[2] * scores[3]



# Read the inputs from a .txt file
lines = None
with open("Day8.txt", "r") as file:
    lines = file.readlines()

# Remove the \n character from each line in the input
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()


visible = 0
for r, row in enumerate(lines):
    for c, value in enumerate(row):
        if is_visible(r, c, lines, value):
            visible += 1

# Print the answer to part 1
print(visible)


max_score = 0    
for r, row in enumerate(lines):
    for c, value in enumerate(row):
        max_score = max(compute_scenic_score(r, c, lines, value), max_score)

# Print the answer to part 2
print(max_score)