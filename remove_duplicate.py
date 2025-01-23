# Read the input file and remove duplicates
def remove_duplicates(input_file, output_file):
    seen = set()  # To keep track of unique lines
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Check if the line has already been seen
            if line not in seen:
                outfile.write(line)  # Write unique lines to the output file
                seen.add(line)  # Mark the line as seen

# Example usage
# change file.txt
remove_duplicates('file.txt', 'output.txt')

print("Duplicates removed. Unique lines saved in 'output.txt'.")
