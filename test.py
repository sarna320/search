from KMP import find_kmp
from KR import find_karp_rabin
from N import find_naive
import random


def test_naive():
    # Test empty pattern
    assert find_naive("", "abcde") == [0, 1, 2, 3, 4, 5]

    # Test empty text
    assert find_naive("abc", "") == []

    # Test empty pattern i text
    assert find_naive("", "") == [0]

    # Test pattern = text
    assert find_naive("abc", "abc") == [0]

    # Test pattern longer than text
    assert find_naive("abcdef", "abc") == []

    # Test pattern not in text
    assert find_naive("xyz", "abc") == []

    # Test data sets
    assert find_naive("abc", "abcdeabc") == [0, 5]
    assert find_naive("abc", "abcabcabc") == [0, 3, 6]
    assert find_naive("abc", "ababab") == []
    assert find_naive("ab", "ababab") == [0, 2, 4]
    print("Naive passed tests")


def test_algorithms():
    # Setup for generating random texts and patterns
    alphabet = "ab"
    num_tests = 100

    for _ in range(num_tests):
        # Generating random texts and patterns
        text_length = random.randint(1, 100)
        pattern_length = random.randint(1, text_length)
        text = "".join(random.choice(alphabet) for _ in range(text_length))
        pattern = "".join(random.choice(alphabet) for _ in range(pattern_length))

        # Testing Naive, KMP, and Karp-Rabin algorithms
        naive_result = find_naive(pattern, text)
        kmp_result = find_kmp(pattern, text)
        karp_rabin_result = find_karp_rabin(pattern, text)

        # Asserting that KMP and Karp-Rabin results match with Naive algorithm
        assert kmp_result == naive_result
        assert karp_rabin_result == naive_result
    print("KMP and KR passed tests")


if __name__ == "__main__":
    test_naive()
    test_algorithms()
