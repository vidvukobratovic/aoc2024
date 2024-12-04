import re

def process_instructions(file_path):
    total = 0  # Initialize the total sum
    processing = True  # Start in a "do()" state

    # Read the input file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Regex patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # Matches mul(X,Y)
    command_pattern = r"\b(do|don't)\(\)"  # Matches do() or don't()
    
    # Split content into commands and mul patterns
    segments = re.split(command_pattern, content)
    
    for segment in segments:
        segment = segment.strip()
        if segment == "do":
            processing = True
        elif segment == "don't":
            processing = False
        elif processing:
            # Process mul instructions only if in a "do()" state
            matches = re.findall(mul_pattern, segment)
            for x, y in matches:
                total += int(x) * int(y)  # Multiply and add to the total
    
    return total

# Usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with the path to your input file
    result = process_instructions(input_file)
    print(f"The total sum of all valid mul calls is: {result}")

