from util import read_input

problem_input = read_input("04")

lines = problem_input.split("\n")

pairs = map(lambda x: x.split(","), lines)

subsumed = 0
for pair in pairs:
    ranges_str = list(map(lambda x: x.split("-"), pair))
    ranges = list(map(lambda x: list(map(int, x)), ranges_str))
    left = max(ranges[0][0], ranges[1][0])
    right = min(ranges[0][1], ranges[1][1])
    if [left, right] in ranges:
        subsumed += 1

print("Solution part 1:")
print(subsumed)

pairs = map(lambda x: x.split(","), lines)

overlap = 0
for pair in pairs:
    ranges_str = list(map(lambda x: x.split("-"), pair))
    ranges = list(map(lambda x: list(map(int, x)), ranges_str))
    if ranges[0][1] >= ranges[1][0] and ranges[0][0] <= ranges[1][1]:
        overlap += 1

print("Solution part 2:")
print(overlap)

# part 1: 18 minutes
# part 2: 9 minutes
# total: 27 minutes