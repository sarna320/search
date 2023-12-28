def find_naive(string, text):
    # List to store the starting positions where the string is found in the text
    positions = []
    # Length of the string (pattern) and the text
    len_string = len(string)
    len_text = len(text)

    # Iterate over each possible starting position in the text
    for i in range(len_text - len_string + 1):
        # Check if the substring from the current position matches the string
        if text[i : i + len_string] == string:
            # If a match is found, append the starting index to the positions list
            positions.append(i)

    # Return the list of positions where the string was found in the text
    return positions
