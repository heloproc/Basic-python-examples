def is_rotate_pair(word1, word2):
    """Checks if two words are rotate pairs (e.g., 'abc' and 'cab')."""
    if len(word1) != len(word2):
        return False  # Rotate pairs must have the same length
    return word2 in (word1 + word1)  # Efficiently check if word2 is a rotation of word1

def find_rotate_pairs(filename):
    """Finds all rotate pairs in a word list file."""
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip())

    rotate_pairs = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):  # Avoid checking a word against itself
            if is_rotate_pair(words[i], words[j]):
                rotate_pairs.append((words[i], words[j]))

    return rotate_pairs

# Example usage
filename = "words.txt"  # Replace with your word list file
pairs = find_rotate_pairs(filename)

if pairs:
    print("Rotate pairs found:")
    for word1, word2 in pairs:
        print(f"{word1} - {word2}")
else:
    print("No rotate pairs found in the word list.")