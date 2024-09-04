s = "Your input string here"  # Replace with your actual string

# Strip trailing spaces and split the string into words
words = s.strip().split()

# Check if the list is empty (edge case), return 0 if it is
if words:
    last_word_length = len(words[-1])
else:
    last_word_length = 0

print(last_word_length)
