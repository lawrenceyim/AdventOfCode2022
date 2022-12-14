# Parse a string representation of a nested list into a Python list
def parse(string):
    parsed = []
    number = ""
    i = 0
    while i < len(string):
        ch = string[i]
        if ch == "[":
            result, index = parse(string[i + 1:])
            parsed.append(result)
            i += index
        elif ch == "]":
            if number != "":
                parsed.append(int(number))
            return (parsed, i + 1)
        elif ch == ",":
            if number != "":
                parsed.append(int(number))
                number = ""
        else:
            number += ch
        i += 1
    return parsed[0]


# Compare the left and right values to determine if it is in the correct order
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else 0 if left > right else -1
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare(l, r)
            if result != -1:
                return result
        return compare(len(left), len(right))
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])


# Read the inputs from a .txt file
lines = None
with open("Day13.txt", "r") as file:
    lines = file.readlines()

# Clean the input data by removing the \n from the end of each line
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
    
pairs = 0
pairs_index = 1
for i in range(0, len(lines), 3):
    left = parse(lines[i])
    right = parse(lines[i + 1])
    in_order = compare(left, right)
    if in_order == 1:
        pairs += pairs_index
    pairs_index += 1

# Answer to part 1
print(pairs)

# Add all input values to a list
all_values = []
for i in range(0, len(lines), 3):
    left = parse(lines[i])
    right = parse(lines[i + 1])
    all_values.append(left)
    all_values.append(right)

# Add the decoder values to the list
all_values.append([2])
all_values.append([6])

# Iterate over all the values and label them with their respective place in a sorted list
sorted_values = []
for i in range(len(all_values)):
    place = 0
    for j in range(len(all_values)):
        if i == j:
            continue
        if compare(all_values[j], all_values[i]) == 1:
            place += 1
    sorted_values.append((place, all_values[i]))

sorted_values.sort()

# Find the two decoder values
decoder_2 = -1
decoder_6 = -1

# Find the indices of the decoder values
for i, value in enumerate(sorted_values):
    if decoder_2 == -1 and value[1] == [2]:
        decoder_2 = i + 1
    elif value[1] == [6]:
        decoder_6 = i + 1
        break

# Answer to part 2
print(decoder_2 * decoder_6)