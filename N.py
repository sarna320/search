def find_naive(string, text):
    positions = []
    len_string = len(string)
    len_text = len(text)

    for i in range(len_text - len_string + 1):
        if text[i : i + len_string] == string:
            positions.append(i)

    return positions
