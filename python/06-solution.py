from util import read_input

problem_input = read_input("06")

for i in range(len(problem_input)):
    substring = problem_input[i:i+4]
    if len(set(substring)) == 4:
        print(i + 4)
        break


for i in range(len(problem_input)):
    substring = problem_input[i:i+14]
    if len(set(substring)) == 14:
        print(i + 14)
        break

# part 1:  8 minutes
# part 2:  2 minutes
# total: 10 minutes