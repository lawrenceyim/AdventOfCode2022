import copy
import queue

# convert a lower case letter to an integer value
def value_of(ch):
    if ch == "S":
        return 1
    if ch == "E":
        return 26
    return ord(ch) - 96


# Determine whether a move is valid in the a_star search algorithm
def is_valid_move(grid, current, next):
    current_height = value_of(grid[current[0]][current[1]])
    next_height = value_of(grid[next[0]][next[1]])
    if next_height <= current_height + 1:
        return True
    else:
        return False


def distance_from_goal(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1]) 

# Find the number of steps needed for the shortest path
def a_star_search(grid, start, end):
    lowest_step = float("inf")
    lowest_path_from = {}
    lowest_cost = {}

    lowest_path_from[start] = start
    lowest_cost[start] = 0
    
    q = queue.PriorityQueue()

    #      path cost    position
    q.put((0,           start))

    while not q.empty():
        path_cost, position = q.get()
        row = position[0]
        column = position[1]

        # If goal state is found
        if position == end:
            steps = 0
            current = end
            # Retrace the path with the lowest path cost
            while current != start:
                current = lowest_path_from[current]
                steps += 1
            
            lowest_step = min(lowest_step, steps)

        # Expand the state and add its neighbors to the priority queue if applicable    
        if row > 0:
            next = (row - 1, column)
            if is_valid_move(grid, position, next):
                man_dist = distance_from_goal(next, end)
                new_path_cost = path_cost + 1
                if next not in lowest_cost or new_path_cost < lowest_cost[next]:
                    lowest_cost[next] = new_path_cost
                    lowest_path_from[next] = position
                    q.put((new_path_cost + man_dist, next))

        if row < len(grid) - 1:
            next = (row + 1, column)
            if is_valid_move(grid, position, next):
                man_dist = distance_from_goal(next, end)
                new_path_cost = path_cost + 1
                if next not in lowest_cost or new_path_cost < lowest_cost[next]:
                    lowest_cost[next] = new_path_cost
                    lowest_path_from[next] = position
                    q.put((new_path_cost + man_dist, next))

        if column > 0:
            next = (row, column - 1)
            if is_valid_move(grid, position, next):
                man_dist = distance_from_goal(next, end)
                new_path_cost = path_cost + 1
                if next not in lowest_cost or new_path_cost < lowest_cost[next]:
                    lowest_cost[next] = new_path_cost
                    lowest_path_from[next] = position
                    q.put((new_path_cost + man_dist, next))

        if column < len(grid[0]) - 1:
            next = (row, column + 1)
            if is_valid_move(grid, position, next):
                man_dist = distance_from_goal(next, end)
                new_path_cost = path_cost + 1
                if next not in lowest_cost or new_path_cost < lowest_cost[next]:
                    lowest_cost[next] = new_path_cost
                    lowest_path_from[next] = position
                    q.put((new_path_cost + man_dist, next))

    return lowest_step



# Read the inputs from a .txt file
lines = None
with open("Day12.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].rstrip()

    
start = None
end = None
# Find the start and end positions
for i, row in enumerate(lines):
    for j, value in enumerate(row):
        if value == "S":
            start = (i, j)
        if value == "E":
            end = (i, j)

# Answer to part 1
answer = a_star_search(lines, start, end)
print(answer)

# Run an A-star search from every starting point
lowest_step = float("inf")
for i, row in enumerate(lines):
    for j, value in enumerate(row):
        if value == "S" or value == "a":
            start = (i, j)
            answer = a_star_search(lines, start, end)
            lowest_step = min(lowest_step, answer)

# Answer to part 2
print(lowest_step)