from util import read_input


def find_total_calls_per_elf(text: str) -> list[int]:
    elves = text.split(("\n\n"))
    cals_per_elf = [elf.split("\n") for elf in elves]
    cals_per_elf = [[int(cal) for cal in elf] for elf in cals_per_elf]
    total_cals_per_elf = [sum(cals) for cals in cals_per_elf]
    return total_cals_per_elf


problem_input = read_input("01")
cals_per_elf = find_total_calls_per_elf(problem_input)

print("Solution part 1:")
print(max(cals_per_elf))


cals_per_elf.sort(reverse=True)
print("Solution part 2:")
print(sum(cals_per_elf[0:3]))
