def check_increasing_or_decreasing(numbers):
    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    return is_increasing or is_decreasing

def check_adjacent_num_diff(numbers):
    return all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def is_safe_line(line):
    try:
        numbers = list(map(int, line.split()))  # Convert space-separated numbers to a list of integers
        order_check = check_increasing_or_decreasing(numbers)
        diff_check = check_adjacent_num_diff(numbers)
        return order_check and diff_check
    except ValueError:
        return False

def count_safe_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file if is_safe_line(line.strip()))

if __name__ == "__main__":
    file_name = 'input.txt'
    total_safe = count_safe_lines(file_name)
    print(f'Total safe lines: {total_safe}')

