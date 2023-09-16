def create_file_with_content(filename):
    with open(filename, 'w') as file:
        file.write("Neither apple nor pine are in pineapple. Boxing rings are square.\n")
        file.write("Writers write, but fingers don’t fing. Overlook and oversee are opposites.\n")
        file.write("A house can burn up as it burns down. An alarm goes off by going on.\n")

# a) Read back the entire file content using read() and display it
def read_file_using_read(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print("a) Entire file content:")
    print(content)

# b) Append more text to the file and display the content with line numbers
def append_and_display(filename, additional_text):
    with open(filename, 'a') as file:
        file.write(additional_text + '\n')
    with open(filename, 'r') as file:
        content = file.readlines()
    print("\nb) File content with line numbers:")
    for i, line in enumerate(content, start=1):
        print(f"{i}: {line.strip()}")

# c) Display the last line of the file
def display_last_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    last_line = lines[-1]
    print(f"\nc) Last line of the file: {last_line.strip()}")

# d) Display the first line from the 10th character onwards
def display_first_line_from_10th_char(filename):
    with open(filename, 'r') as file:
        first_line = file.readline()
    truncated_line = first_line[9:]
    print(f"\nd) First line from the 10th character onwards: {truncated_line.strip()}")

# e) Read and display a specific line from the file based on user input
def read_specific_line(filename, line_num):
    with open(filename, 'r') as file:
        lines = file.readlines()
    if 1 <= line_num <= len(lines):
        print(f"\ne) Line {line_num}: {lines[line_num - 1].strip()}")
    else:
        print("\ne) Invalid line number.")

# f) Find the frequency of words beginning with each letter
def word_frequency_by_letter(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        words = line.split()
        for word in words:
            # Remove punctuation and convert to lowercase
            word = word.strip('.,!?').lower()
            if word:
                initial_letter = word[0]
                if initial_letter in word_counts:
                    word_counts[initial_letter] += 1
                else:
                    word_counts[initial_letter] = 1
    
    print("\nf) Frequency of words beginning with each letter:")
    for letter, count in sorted(word_counts.items()):
        print(f"Words beginning with {letter}: {count}")

filename = "q1data.txt"
create_file_with_content(filename)
a = "y"
while a == "y":
    op = input("Enter which part of the question you want to do (a-f): ")
    c = op.lower()
    if c == "a":
        read_file_using_read(filename)
    elif c == "b":
        append_and_display(filename, input("Enter text to append: "))
    elif c == "c":
        display_last_line(filename)
    elif c == "d":
        display_first_line_from_10th_char(filename)
    elif c == "e":
        line_num = int(input("Enter the line number to read: "))
        read_specific_line(filename, line_num)
    elif c == "f":
        word_frequency_by_letter(filename)
    else:
        print("Invalid choice.")
    a = input("Do you want to continue? (y/n) ").lower()
