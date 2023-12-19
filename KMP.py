def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def find_kmp(string, text):
    positions = []
    len_string = len(string)
    len_text = len(text)

    lps = compute_lps_array(string)
    i, j = 0, 0

    while i < len_text:
        if string[j] == text[i]:
            i += 1
            j += 1

        if j == len_string:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len_text and string[j] != text[i]:
            if j:
                j = lps[j - 1]
            else:
                i += 1

    return positions
