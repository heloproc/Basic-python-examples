def read_file(filename):
    """Reads a file and returns a list of words."""
    with open(filename, 'r') as f:
        words = f.read().split()
    return words

def create_markov_chain(words, prefix_length=2):
    """Creates a Markov chain dictionary.

    Args:
        words: A list of words from the text.
        prefix_length: The length of the prefix (default is 2).

    Returns:
        A dictionary representing the Markov chain.
    """
    markov_chain = {}
    for i in range(len(words) - prefix_length):
        prefix = tuple(words[i:i + prefix_length]) # Tuple of prefix words
        suffix = words[i + prefix_length]
        if prefix in markov_chain:
            markov_chain[prefix].append(suffix)
        else:
            markov_chain[prefix] = [suffix]
    return markov_chain

filename = "your_text_file.txt"  # Replace with your file name
words = read_file(filename)
markov_chain = create_markov_chain(words, prefix_length=2)

print(markov_chain)