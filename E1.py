# Read the input file
input_filename = "file_to_read.txt"
output_filename = "result.txt"

try:
    with open(input_filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{input_filename}' not found.")
    exit(1)

# Count the occurrences of "terrible" and replace them
words = text.split()
count_terrible = 0

for i in range(len(words)):
    if words[i] == "terrible":
        count_terrible += 1
        if count_terrible % 2 == 0:
            words[i] = "pathetic"
        else:
            words[i] = "marvellous"

# Join the modified words back into a single text
modified_text = ' '.join(words)

# Write the modified text to the output file
try:
    with open(output_filename, 'w') as file:
        file.write(modified_text)
    print(f"Total occurrences of 'terrible': {count_terrible}")
    print(f"Modified text written to '{output_filename}'.")
except IOError:
    print(f"Error writing to '{output_filename}'.")

