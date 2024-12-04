import re

def process_instructions(file_path):
    total = 0  # Initialize the total sum

    # Read the input file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Regex pattern to match valid mul(X,Y) syntax
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches
    matches = re.findall(pattern, content)
    
    # Process each match
    for x, y in matches:
        total += int(x) * int(y)  # Multiply and add to the total
    
    return total

# Usage
if __name__ == "__main__":
    input = "input.txt"
    result = process_instructions(input)
    print(f"Total sum: {result}")

