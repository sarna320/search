def calculate_hash(text, length):
    hash_value = 0
    prime = 101  # A prime number

    for i in range(length):
        hash_value = (hash_value * 256 + ord(text[i])) % prime

    return hash_value


def find_karp_rabin(string, text):
    positions = []
    len_string = len(string)
    len_text = len(text)
    prime = 101  # A prime number
    hash_string = calculate_hash(string, len_string)
    hash_text = calculate_hash(text, len_string)

    for i in range(len_text - len_string + 1):
        if hash_string == hash_text:
            if text[i : i + len_string] == string:
                positions.append(i)

        if i < len_text - len_string:
            hash_text = (
                256 * (hash_text - ord(text[i]) * (256 ** (len_string - 1)))
                + ord(text[i + len_string])
            ) % prime

    return positions
