import itertools

# makes from file 

# Read words from the first file
with open('Passwords.txt', 'r') as file1:
    words1 = [line.strip() for line in file1]

# Read words from the second file
with open('Usernames.txt', 'r') as file2:
    words2 = [line.strip() for line in file2]

# Generate all combinations of words from the two files
combinations = itertools.product(words1, words2)

# Write the combinations to an output file
with open('output.txt', 'w') as output:
    for combo in combinations:
        output.write(f"{combo[0]} {combo[1]}\n")

print("All combinations have been written to 'output.txt'.")


# Open the input file for reading
with open('output.txt', 'r') as infile:
    # Open the two output files for writing
    with open('left_words.txt', 'w') as left_file, open('right_words.txt', 'w') as right_file:
        # Process each line in the input file
        for line in infile:
            # Split the line into two parts using space as a delimiter
            left_word, right_word = line.strip().split(' ', 1)  # Split at the first space
            # Write the left word to the first file and the right word to the second file
            left_file.write(left_word + '\n')
            right_file.write(right_word + '\n')

print("The words have been separated into 'left_words.txt' and 'right_words.txt'.")
