import random

def read_file(filename):
    """Reads a file and returns a list of words."""
    with open(filename, 'r') as f:
        words = f.read().split()
    return words

def create_markov_chain(words, prefix_length=2):
    """Creates a Markov chain dictionary."""
    markov_chain = {}
    for i in range(len(words) - prefix_length):
        prefix = tuple(words[i:i + prefix_length])
        suffix = words[i + prefix_length]
        if prefix in markov_chain:
            markov_chain[prefix].append(suffix)
        else:
            markov_chain[prefix] = [suffix]
    return markov_chain

def generate_text(chain, length=100, prefix_length=2):
    """Generates random text based on a Markov chain.

    Args:
        chain: The Markov chain dictionary.
        length: The desired length of the generated text (in words).

    Returns:
        A string of randomly generated text.
    """
    current_prefix = random.choice(list(chain.keys())) # Start with a random prefix
    text = list(current_prefix)

    for _ in range(length - len(current_prefix)):
        possible_suffixes = chain.get(current_prefix, [])
        if possible_suffixes:
            next_word = random.choice(possible_suffixes)
            text.append(next_word)
            current_prefix = tuple(text[-prefix_length:])  # Update the prefix
        else:
            break  # Stop if we reach a dead end in the chain

    return ' '.join(text)  # Join the words into a string

# Example usage
filename = "file.txt"  # Replace with your file name
words = read_file(filename)
markov_chain = create_markov_chain(words, prefix_length=2)

# Generate and print random text
random_text = generate_text(markov_chain, length=100)
print(random_text)
