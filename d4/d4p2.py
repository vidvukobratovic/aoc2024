def load_and_pad(filename, pad_len):
    grid = []
    with open(filename, "rt") as f:
        for line in f:
            grid.append(line.strip() + "." * pad_len)

    for _ in range(pad_len):
        grid.append("." * len(grid[0]))

    return grid

def part_2(grid):
    n_rows, n_cols = len(grid), len(grid[0])
    cross_hits = 0

    for r in range(n_rows - 3):
        for c in range(n_cols - 3):
            if grid[r][c] != "A":
                continue
            if (
                (grid[r - 1][c - 1] == "M" and grid[r + 1][c + 1] == "S")
                or (grid[r - 1][c - 1] == "S" and grid[r + 1][c + 1] == "M")
            ) and (
                (grid[r - 1][c + 1] == "M" and grid[r + 1][c - 1] == "S")
                or (grid[r - 1][c + 1] == "S" and grid[r + 1][c - 1] == "M")
            ):
                cross_hits += 1

    return cross_hits


def main():
    grid = load_and_pad("input.txt", pad_len=3)
    print(f"Part 1: {part_1(grid)}")


if __name__ == "__main__":
    main()
