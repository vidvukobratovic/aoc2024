def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def count_word_in_direction(grid, word, start_row, start_col, direction):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    dr, dc = direction
    count = 0

    # Check if the word fits in the given direction
    for i in range(word_len):
        r, c = start_row + dr * i, start_col + dc * i
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
            return 0  # Word does not fit
    
    return 1  # Word found

def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # top-left diagonal
        (-1, 1),  # top-right diagonal
        (1, -1),  # bottom-left diagonal
        (1, 1),   # bottom-right diagonal
    ]
    count = 0

    # Traverse every cell in the grid
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == word[0]:  # Start search if first letter matches
                for direction in directions:
                    count += count_word_in_direction(grid, word, row, col, direction)
    
    return count

if __name__ == "__main__":
    # Read the input
    grid = read_input("input.txt")
    word = "XMAS"

    # Find and count occurrences of the word
    occurrences = find_word(grid, word)
    print(f"The word '{word}' appears {occurrences} times in the word search.")

