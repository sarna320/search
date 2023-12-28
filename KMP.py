def compute_lps_array(pattern):
    # Length of the pattern
    m = len(pattern)
    # Longest Prefix Suffix (LPS) array for the pattern
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1

    # Loop to fill in the LPS array
    while i < m:
        if pattern[i] == pattern[length]:
            # If characters match, increment length and set LPS value
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length:
                # If length is not 0, update it to the previous longest prefix suffix
                length = lps[length - 1]
            else:
                # If length is 0, set LPS[i] to 0 and move to the next character
                lps[i] = 0
                i += 1

    # Return the completed LPS array
    return lps


def find_kmp(string, text):
    # List to store positions where the string is found in the text
    positions = []
    # Lengths of the string and text
    len_string = len(string)
    len_text = len(text)

    # Compute the LPS array for the string
    lps = compute_lps_array(string)
    i, j = 0, 0  # Pointers for text and string

    # Loop to scan the text
    while i < len_text:
        if string[j] == text[i]:
            # If characters match, increment both pointers
            i += 1
            j += 1

        # If the entire string is found, add its starting position to the list
        if j == len_string:
            positions.append(i - j)
            # Update the value of j based on the last character of the found string
            j = lps[j - 1]
        elif i < len_text and string[j] != text[i]:
            # If characters do not match
            if j:
                # Update the value of j using the LPS array
                j = lps[j - 1]
            else:
                # Move to the next character in the text
                i += 1

    # Return the list of positions where the string was found in the text
    return positions
