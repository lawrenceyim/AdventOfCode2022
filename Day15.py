import collections

# Compute the Manhattan distance between two point
def compute_distance(input):
    return abs(input[0] - input[2]) + abs(input[1] - input[3])


# Find the spaces on a specific row where a beacon cannot be located
def find_spaces(input, row_to_check):
    manhattan_distance = compute_distance(input)
    invalid_spaces = []
    columns_to_check = (input[1] - manhattan_distance, input[1] + manhattan_distance)
    
    for column in range(columns_to_check[0], columns_to_check[1] + 1):
        distance = compute_distance((input[0], input[1], row_to_check, column))
        if distance <= manhattan_distance:
            invalid_spaces.append((row_to_check,column))

    return invalid_spaces


# Check if a value is within the allowed search space
def within_search_space(value, search_size):
    return value >= 0 and value <= search_size


# Find the values one space outside the perimeter of a sensor's coverage
def get_perimeter_values(sensor, search_size):
    values = []
    rows_to_check = [sensor[0] - sensor[2], sensor[0] + sensor[2]]

    if within_search_space(rows_to_check[0] - 1, search_size) and within_search_space(sensor[1], search_size):
        values.append((rows_to_check[0] - 1, sensor[1]))
    if within_search_space(rows_to_check[0] + 1, search_size) and within_search_space(sensor[1], search_size):
        values.append((rows_to_check[1] + 1, sensor[1]))

    for row in range(rows_to_check[0], rows_to_check[1] + 1):
        if not within_search_space(row, search_size):
            continue

        offset = sensor[2] - abs(sensor[0] - row) + 1

        if within_search_space(sensor[1] - offset, search_size):
            values.append((row, sensor[1] - offset))
        if within_search_space(sensor[1] + offset, search_size):
            values.append((row, sensor[1] + offset))

    return values


# Determine is a (row, column) value is within the coverage of another sensor
def detected_by_another_sensor(value, sensor):
    for sensor in sensors:
        distance = compute_distance((value[0], value[1], sensor[0], sensor[1]))
        if distance <= sensor[2]:
            return True
    return False


# Read the inputs from a .txt file
lines = None
with open("Day15.txt", "r") as file: 
    lines = file.readlines()

# Check how many spaces a beacon cannot exist in this row
row_to_check = 2000000

# Contain all the spots where a beacon cannot exist
spaces_without_beacons = set()

# Contain all the columns occupied by a beacon or a sensor
occupied = set()

# Record all inputs into a list
inputs = []
for line in lines:
    words = line.split(" ")
    sensor_x = int(words[2][2:-1])
    sensor_y = int(words[3][2:-1])
    beacon_x = int(words[8][2:-1])
    beacon_y = int(words[9][2:])
    inputs.append((sensor_y, sensor_x, beacon_y, beacon_x))
    occupied.add((sensor_y, sensor_x))
    occupied.add((beacon_y, beacon_x))

# Iterate over the input to find the spaces where a beacon cannot be located
for input in inputs:
    invalid_spaces = find_spaces(input, row_to_check)
    for space in invalid_spaces:
        if space not in occupied:
            spaces_without_beacons.add(space)

# Answer to part 1
print(len(spaces_without_beacons))

# # Size of the area to search
search_size = 4000000

# Iterate over the input to find the Manhattan distance of each sensor
sensors = []
for input in inputs:
    sensors.append((input[0], input[1], compute_distance(input)))

# Store all the possible answers
possible_answers = []

# Find all possible answers for part 2
for sensor in sensors:
    perimeter_plus_one = get_perimeter_values(sensor, search_size)
    for value in perimeter_plus_one:
        is_detected = detected_by_another_sensor(value, sensors)
        if not is_detected:
            tuning_frequency = 4000000 * value[1] + value[0]
            possible_answers.append(tuning_frequency)
            break

# Answer to part 2
print(collections.Counter(possible_answers).most_common(1)[0][0])