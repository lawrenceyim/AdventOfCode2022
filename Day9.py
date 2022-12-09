"""
Inputs:
    direction, str - the direction to move the knot in
    position, list(int, int) - the X and Y position of the knot
Return:
    list(int, int) - the X and Y position of the knot after it has been moved
"""
def move(direction, position):
    if direction == "U":
        position[1] += 1
    elif direction == "D":
        position[1] -= 1
    elif direction == "L":
        position[0] -= 1
    elif direction == "R":
        position[0] += 1
    elif direction == "UL":
        position[0] -= 1
        position[1] += 1
    elif direction == "UR":
        position[0] += 1
        position[1] += 1
    elif direction == "DL":
        position[0] -= 1
        position[1] -= 1
    elif direction == "DR":
        position[0] += 1
        position[1] -= 1
    return position

"""
Inputs:
    head, list(int, int) - the X and Y position of the head knot
    tail, list(int, int) - the X and Y position of the tail knot
Return:
    str - the direction that the knot should be moved in
"""
def compute_tail_direction(head, tail):
    x_diff = abs(head[0] - tail[0])
    y_diff = abs(head[1] - tail[1])
    
    # If the tail is touching the head
    if x_diff <= 1 and y_diff <= 1:
        return ""

    if x_diff == 0 and y_diff > 1:
        if head[1] > tail[1]:
            return "U"
        elif head[1] < tail[1]:
            return "D"
    
    elif x_diff > 1 and y_diff == 0:
        if head[0] > tail[0]:
            return "R"
        elif head[0] < tail[0]:
            return "L"

    else:
        if head[0] > tail[0]:
            if head[1] > tail[1]:
                return "UR"
            else:
                return "DR"
        else:
            if head[1] > tail[1]:
                return "UL"
            else:
                return "DL"

# Read the inputs from a .txt file
lines = None
with open("Day9.txt", "r") as file:
    lines = file.readlines()


# Part 1

# Initialize the position of the head and tail knot
head = [0, 0]
tail = [0, 0]

# Initialize a set to store the unique positions that the tail knot has been at
tail_positions = set()

for line in lines:
    words = line.split(" ")
    head_direction = words[0]
    moves = int(words[1])
    for i in range(moves):
        head = move(head_direction, head)
        tail_direction = compute_tail_direction(head, tail)
        tail = move(tail_direction, tail)
        tail_positions.add(tuple(tail))

# Print the answer to part 1
print(len(tail_positions))


# Part 2
tail_positions = set()

# Initialize the starting positions of all ten knots plus an extra pseudo-knot that is only needed to simplify the code
knots = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

for line in lines:
    words = line.split(" ")
    head_direction = words[0]
    moves = int(words[1])
    for i in range(moves):
        # Set the initial direction to the direction provided by the inputs
        direction = head_direction
        # Iterate over all ten knots
        for j in range(10):
            knots[j] = move(direction, knots[j])
            direction = compute_tail_direction(knots[j], knots[j + 1])
        tail_positions.add(tuple(knots[9]))

# Print the answer to part 2
print(len(tail_positions))
