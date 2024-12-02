with open('input.txt', 'r') as file:
    total_difference = 0
    left_numbers = []
    right_numbers = []

    for line in file:
        numbers = line.split('  ')
        left_numbers.append(int(numbers[0]))
        right_numbers.append(int(numbers[1]))

left_numbers.sort()
right_numbers.sort()

for left, right in zip(left_numbers, right_numbers):
    total_difference += abs(left-right)

print(f'Total difference: {total_difference}')
