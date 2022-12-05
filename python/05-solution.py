from util import read_input
import numpy as np

problem_input = read_input("05")

lines: list[str] = problem_input.split("\n")

input_split_line_index = lines.index("")

stacks_rows = lines[:input_split_line_index-1]
moves = lines[input_split_line_index+1:]

stacks_rows_clean = []
for stacks_row in stacks_rows:
    stacks_row_clean = []
    for i in range(1, len(stacks_rows[input_split_line_index-2]), 4):
        stacks_row_clean.append(stacks_row[i])

    stacks_rows_clean.append(stacks_row_clean)


stacks_array: np.ndarray = np.array(stacks_rows_clean)
stacks = np.flip(stacks_array.T, 1).tolist()

nonempty = lambda x: list(filter(lambda y: y != ' ', x))
stacks = list(map(nonempty, stacks))

for move in moves:
    match move.split():
        case ["move", count, "from", source, "to", drain]:
            count = int(count)
            source = int(source) - 1
            drain = int(drain) - 1
            for _ in range(count):
                stacks[drain].append(stacks[source].pop())
        case _:
            print("Couldn't match on this:")
            print(move)

solution = "".join(map(lambda x: x.pop(), stacks))
print(solution)



stacks_array: np.ndarray = np.array(stacks_rows_clean)
stacks = np.flip(stacks_array.T, 1).tolist()

nonempty = lambda x: list(filter(lambda y: y != ' ', x))
stacks = list(map(nonempty, stacks))

for move in moves:
    match move.split():
        case ["move", count, "from", source, "to", drain]:
            count = int(count)
            source = int(source) - 1
            drain = int(drain) - 1
            stacks_source = stacks[source][:-count]
            stacks_drain = stacks[drain] + stacks[source][-count:]
            stacks[source] = stacks_source
            stacks[drain] = stacks_drain
        case _:
            print("Couldn't match on this:")
            print(move)

solution = "".join(map(lambda x: x.pop(), stacks))
print(solution)


# part 1:  35 minutes
# part 2:  4 minutes
# total: minutes