from KMP import *
from KR import *
from N import *

import random
import string


def test_naive():
    # Test pustego wzorca
    assert find_naive("", "abcde") == [0, 1, 2, 3, 4, 5]

    # Test pustego tekstu
    assert find_naive("abc", "") == []

    # Test pustego wzorca i tekstu
    assert find_naive("", "") == [0]

    # Test wzorca równego tekstowi
    assert find_naive("abc", "abc") == [0]

    # Test wzorca dłuższego od tekstu
    assert find_naive("abcdef", "abc") == []

    # Test wzorca nie występującego w tekście
    assert find_naive("xyz", "abc") == []

    # Kilka zestawów danych testowych
    assert find_naive("abc", "abcdeabc") == [0, 5]
    assert find_naive("abc", "abcabcabc") == [0, 3, 6]
    assert find_naive("abc", "ababab") == []
    assert find_naive("ab", "ababab") == [0, 2, 4]
    print("Naive passed tests")


def test_algorithms():
    alphabet = "ab"
    num_tests = 100

    for _ in range(num_tests):
        text_length = random.randint(1, 100)
        pattern_length = random.randint(1, text_length)
        text = "".join(random.choice(alphabet) for _ in range(text_length))
        pattern = "".join(random.choice(alphabet) for _ in range(pattern_length))

        naive_result = find_naive(pattern, text)
        kmp_result = find_kmp(pattern, text)
        karp_rabin_result = find_karp_rabin(pattern, text)

        # Porównaj wyniki z algorytmem naiwnym
        assert kmp_result == naive_result
        assert karp_rabin_result == naive_result
    print("KMP and KR passed tests")


if __name__ == "__main__":
    test_naive()
    test_algorithms()
