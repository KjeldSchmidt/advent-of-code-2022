from util import read_input

problem_input = read_input("02")

lines = problem_input.split("\n")
throws = [list(map(ord, line.split())) for line in lines]


def part_1(throws):
    throws_num = list(map(lambda x: (x[0] - 64, x[1] - 87), throws))
    throw_diff = list(map(lambda x: x[1] - x[0], throws_num))

    result_score = sum(map(lambda x: ((x + 1) % 3) * 3, throw_diff))
    symbol_score = sum(list(zip(*throws_num))[1])

    total_score = result_score + symbol_score

    print("Solution Part 1")
    print(f"{symbol_score=}")
    print(f"{result_score=}")
    print(f"{total_score=}")


def part_2(throws):
    throws_num = map(lambda x: (x[0] - 64, x[1] - 87), throws)
    opponent_throws, results = zip(*throws_num)

    magic_map = {1: 1, 2: -1, 3: 0}
    throw_mod = zip(opponent_throws, map(lambda x: magic_map[x], results))
    symbol_scores = map(lambda x: (x[0] + x[1]) % 3 + 1, throw_mod)

    symbol_score = sum(symbol_scores)
    result_score = (sum(results) - len(results)) * 3
    total_score = result_score + symbol_score

    print("Solution Part 2")
    print(f"{result_score=}")
    print(f"{symbol_score=}")
    print(f"{total_score=}")

    # Throw diff

part_1(throws)
print()
part_2(throws)