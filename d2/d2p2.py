def check_increasing_or_decreasing(numbers):
    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    return is_increasing or is_decreasing

def check_adjacent_num_diff(numbers):
    return all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def is_safe_after_removal(numbers):
    for i in range(len(numbers)):
        reduced_numbers = numbers[:i] + numbers[i + 1:]  # Remove the i-th number
        if check_increasing_or_decreasing(reduced_numbers) and check_adjacent_num_diff(reduced_numbers):
            return True
    return False

def is_safe_line(line):
    try:
        numbers = list(map(int, line.split()))  # Convert space-separated numbers to a list of integers
        # Check the original rules first
        if check_increasing_or_decreasing(numbers) and check_adjacent_num_diff(numbers):
            return True
        # If not safe, check if removing one level can make it safe
        is_safe_with_removal = is_safe_after_removal(numbers)
        return is_safe_with_removal
    except ValueError:
        return False

def count_safe_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file if is_safe_line(line.strip()))

if __name__ == "__main__":
    file_name = 'input.txt'
    total_safe = count_safe_lines(file_name)
    print(f'Total safe lines: {total_safe}')

