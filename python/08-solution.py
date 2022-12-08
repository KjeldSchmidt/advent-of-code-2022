import numpy as np

from util import read_input

problem_input = read_input("08").split("\n")
forest: np.ndarray = np.array([[int(digit) for digit in line] for line in problem_input])


def visible_trees_from_left(forest) -> list[tuple[int, int]]:
    visible_trees = []
    for idx, row in enumerate(forest):
        max_tree = -1
        for jdx, tree in enumerate(row):
            if tree > max_tree:
                visible_trees.append((idx, jdx))
                max_tree = tree
    return visible_trees


left = visible_trees_from_left(forest)
top = list(map(lambda x: (x[1], x[0]), visible_trees_from_left(forest.T)))
right = list(map(lambda x: (x[0], len(forest[0]) - 1 - x[1]), visible_trees_from_left(np.flip(forest, 1))))
bottom = list(map( lambda x: (len(forest[0]) - 1 - x[1], x[0]), visible_trees_from_left(np.flip(forest, 0).T)))

unique_trees = list({*left, *top, *right, *bottom})
unique_trees.sort()

print("Solution Part 1:")
print(len(unique_trees))


def find_view_block_right(forest, x, y):
    tree_height = forest[x, y]
    distance = 0
    for i in range(y+1, len(forest[0])):
        distance+= 1
        if forest[x, i] >= tree_height:
            break
    return distance


def find_view_block_left(forest, x, y):
    tree_height = forest[x, y]
    distance = 0
    for i in range(y-1, -1, -1):
        distance+= 1
        if forest[x, i] >= tree_height:
            break
    return distance


def find_view_block_bottom(forest, x, y):
    tree_height = forest[x, y]
    distance = 0
    for i in range(x+1, len(forest)):
        distance+= 1
        if forest[i, y] >= tree_height:
            break
    return distance


def find_view_block_top(forest, x, y):
    tree_height = forest[x, y]
    distance = 0
    for i in range(x-1, -1, -1):
        distance+= 1
        if forest[i, y] >= tree_height:
            break
    return distance


highest_score = 0
for idx, row in enumerate(forest):
    max_tree = -1
    for jdx, tree in enumerate(row):
        score = find_view_block_top(forest, idx, jdx)
        score *= find_view_block_right(forest, idx, jdx)
        score *= find_view_block_left(forest, idx, jdx)
        score *= find_view_block_bottom(forest, idx, jdx)

        highest_score = max(score, highest_score)


print("Solution part 2:")
print(highest_score)

# part 1:  46 minutes
# part 2:  12 minutes
# total: 58 minutes