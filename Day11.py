# Starting item of each monkey
monkeys = []
monkeys.append([92, 73, 86, 83, 65, 51, 55, 93])
monkeys.append([99, 67, 62, 61, 59, 98])
monkeys.append([81, 89, 56, 61, 99])
monkeys.append([97, 74, 68])
monkeys.append([78, 73])
monkeys.append([50])
monkeys.append([95, 88, 53, 75])
monkeys.append([50, 77, 98, 85, 94, 56, 89])

# How the monkey reassess your worry level for an item
operations = []
operations.append(lambda a: a * 5)
operations.append(lambda a: a * a)
operations.append(lambda a: a * 7)
operations.append(lambda a: a + 1)
operations.append(lambda a: a + 3)
operations.append(lambda a: a + 5)
operations.append(lambda a: a + 8)
operations.append(lambda a: a + 2)

# How the monkey decides which monkey to pass an item to
tests = []
tests.append(lambda a: 3 if a % 11 == 0 else 4)
tests.append(lambda a: 6 if a % 2 == 0 else 7)
tests.append(lambda a: 1 if a % 5 == 0 else 5)
tests.append(lambda a: 2 if a % 17 == 0 else 5)
tests.append(lambda a: 2 if a % 19 == 0 else 3)
tests.append(lambda a: 1 if a % 7 == 0 else 6)
tests.append(lambda a: 0 if a % 3 == 0 else 7)
tests.append(lambda a: 4 if a % 13 == 0 else 0)

# Number of items that a monkey inspected
inspected = [0] * len(monkeys)

NUMBER_OF_ROUNDS = 20
for i in range(NUMBER_OF_ROUNDS):
    for j in range(len(monkeys)):
        while len(monkeys[j]) > 0:
            item = monkeys[j].pop(0)
            item = operations[j](item) // 3
            inspected[j] += 1
            to_monkey = tests[j](item)
            monkeys[to_monkey].append(item)

inspected = sorted(inspected)
answer = inspected[-1] * inspected[-2]

# Answer to part 1
print(answer)

# Reset the starting items of the monkeys
monkeys = []
monkeys.append([92, 73, 86, 83, 65, 51, 55, 93])
monkeys.append([99, 67, 62, 61, 59, 98])
monkeys.append([81, 89, 56, 61, 99])
monkeys.append([97, 74, 68])
monkeys.append([78, 73])
monkeys.append([50])
monkeys.append([95, 88, 53, 75])
monkeys.append([50, 77, 98, 85, 94, 56, 89])

inspected = [0] * len(monkeys)
NUMBER_OF_ROUNDS = 10_000
PRODUCT_OF_MODS = 11 * 2 * 5 * 17 * 19 * 7 * 3 * 13

for i in range(NUMBER_OF_ROUNDS):
    for j in range(len(monkeys)):
        while len(monkeys[j]) > 0:
            item = monkeys[j].pop(0) % PRODUCT_OF_MODS
            item = operations[j](item) 
            inspected[j] += 1
            to_monkey = tests[j](item)
            monkeys[to_monkey].append(item)

inspected = sorted(inspected)
answer = inspected[-1] * inspected[-2]

# Answer to part 2
print(answer)