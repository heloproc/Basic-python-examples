def right_justify(s):
    """Right justifies a string to 70 characters."""
    l = []
    for i in s:
        l.append(i)

    pos = 70 - len(l)  # Calculate number of spaces here
                       #the last character appears at 70th column of screen
    justified_string = " " * pos + "".join(l)  # Create justified string
    return justified_string  # Return the justified string


inp = input("Enter a string: ")
print(right_justify(inp))
