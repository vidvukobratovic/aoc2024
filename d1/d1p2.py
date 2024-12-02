from collections import Counter

with open('input.txt', 'r') as file:
    left_numbers = []
    right_numbers = []
    
    for line in file:
        numbers = line.split('  ')
        left_numbers.append(int(numbers[0]))
        right_numbers.append(int(numbers[1]))

right_counts = Counter(right_numbers)

s_score = 0
for num in left_numbers:
    s_score += int(num) * right_counts.get(int(num), 0)

print(f'Similarity score: {s_score}')
