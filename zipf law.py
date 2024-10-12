import math
import matplotlib.pyplot as plt

def read_file(filename):
    """Reads a file and returns a list of lowercase words."""
    with open(filename, 'r') as file:
        words = file.read().lower().split()
    return words

def calculate_zipfs_law(words):
    """Calculates and plots log(frequency) vs log(rank) for words."""
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    ranks = []
    log_frequencies = []
    log_ranks = []

    for rank, (word, frequency) in enumerate(sorted_word_counts, 1):
        log_f = math.log(frequency)
        log_r = math.log(rank)
        ranks.append(rank)
        log_frequencies.append(log_f)
        log_ranks.append(log_r)
        print(f"Word: {word}, log(f): {log_f:.4f}, log(r): {log_r:.4f}")

    # Plot using matplotlib
    plt.plot(log_ranks, log_frequencies, marker='o', linestyle='-')
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.title("Zipf's Law Visualization")
    plt.grid(True)
    plt.show()

    # Estimate s (slope of the line)
    # You can use more sophisticated methods for slope estimation if needed
    s_estimate = -(log_frequencies[0] - log_frequencies[-1]) / (log_ranks[0] - log_ranks[-1])
    print(f"Estimated value of s: {s_estimate:.4f}")

# Example usage
filename = "your_text_file.txt"  # Replace with your file name
words = read_file(filename)
calculate_zipfs_law(words)