from KMP import find_kmp
from KR import find_karp_rabin
from N import find_naive
import random


def test_naive():
    # Test empty pattern
    result = find_naive("", "abcde")
    print(f"find_naive('', 'abcde') = {result}")
    assert find_naive("", "abcde") == [0, 1, 2, 3, 4, 5]

    # Test empty text
    result = find_naive("abc", "")
    print(f"find_naive('abc', '') = {result}")
    assert find_naive("abc", "") == []

    # Test empty pattern i text
    result = find_naive("", "")
    print(f"find_naive('', '') = {result}")
    assert find_naive("", "") == [0]

    # Test pattern = text
    result = find_naive("abc", "abc")
    print(f"find_naive('abc', 'abc') = {result}")
    assert find_naive("abc", "abc") == [0]

    # Test pattern longer than text
    result = find_naive("abcdef", "abc")
    print(f"find_naive('abcdef', 'abc') = {result}")
    assert find_naive("abcdef", "abc") == []

    # Test pattern not in text
    result = find_naive("xyz", "abc")
    print(f"find_naive('xyz', 'abc') = {result}")
    assert find_naive("xyz", "abc") == []

    # Test data sets
    result = find_naive("abc", "abcdeabc")
    print(f"find_naive('abc', 'abcdeabc') = {result}")
    assert find_naive("abc", "abcdeabc") == [0, 5]

    result = find_naive("abc", "abcabcabc")
    print(f"find_naive('abc', 'abcabcabc') = {result}")
    assert find_naive("abc", "abcabcabc") == [0, 3, 6]

    result = find_naive("abc", "ababab")
    print(f"find_naive('abc', 'ababab') = {result}")
    assert find_naive("abc", "ababab") == []

    result = find_naive("ab", "ababab")
    print(f"find_naive('ab', 'ababab') = {result}")
    assert find_naive("ab", "ababab") == [0, 2, 4]
    print("Naive passed tests")


def test_KMP():
    # Test empty pattern
    result = find_kmp("", "abcde")
    print(f"find_kmp('', 'abcde') = {result}")
    assert find_kmp("", "abcde") == [0, 1, 2, 3, 4, 5]

    # Test empty text
    result = find_kmp("abc", "")
    print(f"find_kmp('abc', '') = {result}")
    assert find_kmp("abc", "") == []

    # Test empty pattern and text
    result = find_kmp("", "")
    print(f"find_kmp('', '') = {result}")
    assert find_kmp("", "") == [0]

    # Test pattern equals text
    result = find_kmp("abc", "abc")
    print(f"find_kmp('abc', 'abc') = {result}")
    assert find_kmp("abc", "abc") == [0]

    # Test pattern longer than text
    result = find_kmp("abcdef", "abc")
    print(f"find_kmp('abcdef', 'abc') = {result}")
    assert find_kmp("abcdef", "abc") == []

    # Test pattern not in text
    result = find_kmp("xyz", "abc")
    print(f"find_kmp('xyz', 'abc') = {result}")
    assert find_kmp("xyz", "abc") == []

    # Test data sets
    result = find_kmp("abc", "abcdeabc")
    print(f"find_kmp('abc', 'abcdeabc') = {result}")
    assert find_kmp("abc", "abcdeabc") == [0, 5]

    result = find_kmp("abc", "abcabcabc")
    print(f"find_kmp('abc', 'abcabcabc') = {result}")
    assert find_kmp("abc", "abcabcabc") == [0, 3, 6]

    result = find_kmp("abc", "ababab")
    print(f"find_kmp('abc', 'ababab') = {result}")
    assert find_kmp("abc", "ababab") == []

    result = find_kmp("ab", "ababab")
    print(f"find_kmp('ab', 'ababab') = {result}")
    assert find_kmp("ab", "ababab") == [0, 2, 4]

    print("KMP passed tests")


def test_kr():
    # Test empty pattern
    result = find_karp_rabin("", "abcde")
    print(f"find_karp_rabin('', 'abcde') = {result}")
    assert find_karp_rabin("", "abcde") == [0, 1, 2, 3, 4, 5]

    # Test empty text
    result = find_karp_rabin("abc", "")
    print(f"find_karp_rabin('abc', '') = {result}")
    assert find_karp_rabin("abc", "") == []

    # Test empty pattern and text
    result = find_karp_rabin("", "")
    print(f"find_karp_rabin('', '') = {result}")
    assert find_karp_rabin("", "") == [0]

    # Test pattern equals text
    result = find_karp_rabin("abc", "abc")
    print(f"find_karp_rabin('abc', 'abc') = {result}")
    assert find_karp_rabin("abc", "abc") == [0]

    # Test pattern longer than text
    result = find_karp_rabin("abcdef", "abc")
    print(f"find_karp_rabin('abcdef', 'abc') = {result}")
    assert find_karp_rabin("abcdef", "abc") == []

    # Test pattern not in text
    result = find_karp_rabin("xyz", "abc")
    print(f"find_karp_rabin('xyz', 'abc') = {result}")
    assert find_karp_rabin("xyz", "abc") == []

    # Test data sets
    result = find_karp_rabin("abc", "abcdeabc")
    print(f"find_karp_rabin('abc', 'abcdeabc') = {result}")
    assert find_karp_rabin("abc", "abcdeabc") == [0, 5]

    result = find_karp_rabin("abc", "abcabcabc")
    print(f"find_karp_rabin('abc', 'abcabcabc') = {result}")
    assert find_karp_rabin("abc", "abcabcabc") == [0, 3, 6]

    result = find_karp_rabin("abc", "ababab")
    print(f"find_karp_rabin('abc', 'ababab') = {result}")
    assert find_karp_rabin("abc", "ababab") == []

    result = find_karp_rabin("ab", "ababab")
    print(f"find_karp_rabin('ab', 'ababab') = {result}")
    assert find_karp_rabin("ab", "ababab") == [0, 2, 4]

    print("Karp-Rabin passed tests")


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
    print(
        "KMP and KR passed tests, all algorithms have same results for random text and pattern,as naive algorithm"
    )


if __name__ == "__main__":
    test_naive()
    print("")
    test_KMP()
    print("")
    test_kr()
    print("")
    test_algorithms()
