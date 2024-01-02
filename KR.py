def calculate_hash(text, length):
    if len(text) < length:
        return 0
    # Initialize hash value to 0
    hash_value = 0
    # Prime number for hashing calculations
    prime = 101

    # Loop to calculate the hash value for the given text
    for i in range(length):
        # Update the hash using ASCII value of the character
        hash_value = (hash_value * 256 + ord(text[i])) % prime

    # Return the calculated hash value
    return hash_value


def find_karp_rabin(string, text):
    # List to store positions where the string is found in the text
    positions = []
    # Lengths of the string and text
    len_string = len(string)
    len_text = len(text)
    # Prime number for hashing calculations
    prime = 101
    # Calculate hash values for the string and the initial substring of the text
    hash_string = calculate_hash(string, len_string)
    hash_text = calculate_hash(text, len_string)

    # Loop to slide the window over the text and check for matches
    for i in range(len_text - len_string + 1):
        # Check if hash values match and if the substrings are identical
        if hash_string == hash_text:
            if text[i : i + len_string] == string:
                # If match is found, add the starting position to the list
                positions.append(i)

        # Update the hash value for the next window
        if i < len_text - len_string:
            hash_text = (
                256 * (hash_text - ord(text[i]) * (256 ** (len_string - 1)))
                + ord(text[i + len_string])
            ) % prime

    # Return the list of positions where the string was found in the text
    return positions
