from util import read_input

problem_input = read_input("03")

lines = problem_input.split("\n")

priority_sum = 0
for line in lines:
    split_at_index = len(line) // 2
    first_half = set(line[:split_at_index])
    second_half = set(line[split_at_index:])
    overlap = list(first_half.intersection(second_half))
    assert len(overlap) == 1
    shared_char: str = overlap[0].swapcase()
    ascii_offset = 64 if shared_char.isupper() else 70
    priority = ord(shared_char) - ascii_offset
    assert 1 <= priority <= 52
    priority_sum += priority

print("Solution part 1")
print(priority_sum)


badge_priority_sum = 0
for i in range(0, len(lines) - 2, 3):
    group = lines[i:i+3]
    badge_candidates = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))
    assert len(badge_candidates) == 1

    badge_type: str = badge_candidates[0].swapcase()
    ascii_offset = 64 if badge_type.isupper() else 70
    priority = ord(badge_type) - ascii_offset
    assert 1 <= priority <= 52
    badge_priority_sum += priority

print("Solution part 2")
print(badge_priority_sum)

# Time Part 1: 16 Minutes
# Tim Part 2: 10 Minutes
# Total Time: 26 minutes