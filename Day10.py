# Read the inputs from a .txt file
lines = None
with open("Day10.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to contain the CPU cycle values
values = [1]
for line in lines:
    words = line.split()
    # Add two cycles to represent an addx instruction
    if "addx" in words:
        values.append(values[-1])
        values.append(values[-1] + int(words[1]))
    # Add one cycle to represent a noop instruction
    else:
        values.append(values[-1])        
    
# Answer to part 1
# Subtract 1 from each cycle index before computing the signal strength
# to get the value during a cycle, not after, since the addx operation adds
# to the value at the end of each cycle and the values represent the value 
# at the end of a cycle
answer = (values[20-1] * 20 + values[60-1] * 60 + values[100-1] * 100 + values[140-1] * 140 + 
          values[180-1] * 180 + values[220-1] * 220)
print(answer) 

# Part 2
ROW_LENGTH = 40

# Instantiate a list to contain the pixels
pixels = []

for i in range(0, 240):
    index =  i % ROW_LENGTH
    register = values[i]
    if register == index - 1 or register == index or register == index + 1:
        pixels.append("# ")   
    else:
        pixels.append(". ")

# Answer to part 2 is the letters spelled out in the ASCII         
for i in range(0, 240, ROW_LENGTH):
    result = ""
    for j in range(0, ROW_LENGTH):
        result += pixels[i + j]
    print(result)