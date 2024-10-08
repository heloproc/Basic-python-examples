def is_triple_double(word):
    """
    Tests if a word contains three consecutive double letters.
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2  # Skip to the next potential double letter
        else:
            count = 0  # Reset the count if double letters are not consecutive
            i = i + 1  # Move to the next letter
    return False  # No triple double found