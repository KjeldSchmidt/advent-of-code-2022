from dataclasses import dataclass
from pathlib import Path

from util import read_input

problem_input = read_input("07").split("\n")

@dataclass
class Directory:
    files: list[tuple[str, int]]
    dirs: list[Path]

    def total_size(self) -> int:
        subdirs_size = sum(map(lambda x: directories[x].total_size(), self.dirs))
        files_size = sum(map(lambda x: x[1], self.files))
        return subdirs_size + files_size


directories: (Path, Directory) = {}
current_directory = Path("/")
for line in problem_input:
    match line.split():
        case ["$", "cd", ".."]: current_directory = current_directory.parent
        case ["$", "cd", subdir]: current_directory = current_directory / subdir
        case ["$", "cd", "/"]: current_directory = current_directory.root
        case ["$", "ls"]: directories[current_directory] = Directory([], [])
        case ["dir", subdir]: directories[current_directory].dirs.append(current_directory / subdir)
        case [size, filename]: directories[current_directory].files.append((filename, int(size)))
        case _:
            print("!!!!!!!!!!! CANNOT PARSE LINE !!!!!!!!")
            print(line)
            print()

candidate_sizes = 0
for path, directory in directories.items():
    total_size = directory.total_size()
    if total_size <= 100000:
        candidate_sizes += total_size

print("Solution Part 1:")
print(candidate_sizes)

max_space = 70000000
free_space_needed = 30000000
total_space_used = directories[Path("/")].total_size()
total_space_unused = max_space - total_space_used
space_to_be_cleaned = free_space_needed - total_space_unused

smallest_sufficient_dir = total_space_used
for path, directory in directories.items():
    total_size = directory.total_size()
    if total_size >= space_to_be_cleaned:
        smallest_sufficient_dir = min(smallest_sufficient_dir, total_size)

print("Solution Part 2:")
print(smallest_sufficient_dir)



# part 1:  40 minutes
# part 2:  7 minutes
# total: 47 minutes