def read_input(index: str) -> str:
    with open(f"{index}-input.txt") as file:
        return file.read()


def read_small_input(index: str) -> str:
    with open(f"{index}-input-small.txt") as file:
        return file.read()
