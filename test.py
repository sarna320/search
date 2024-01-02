from KMP import *
from KR import *
from N import *


import random
import string


def test_naive():
    # Test pustego wzorca
    result = find_naive("", "abcde")
    print(f"find_naive('', 'abcde') = {result}")
    assert result == [0, 1, 2, 3, 4, 5]
    
    # Test pustego tekstu
    result = find_naive("abc", "")
    print(f"find_naive('abc', '') = {result}")
    assert result == []

    # Test pustego wzorca i tekstu
    result = find_naive("", "")
    print(f"find_naive('', '') = {result}")
    assert result == [0]

    # Test wzorca równego tekstowi
    result = find_naive("abc", "abc")
    print(f"find_naive('abc', 'abc') = {result}")
    assert result == [0]

    # Test wzorca dłuższego od tekstu
    result = find_naive("abcdef", "abc")
    print(f"find_naive('abcdef', 'abc') = {result}")
    assert result == []

    # Test wzorca nie występującego w tekście
    result = find_naive("xyz", "abc")
    print(f"find_naive('xyz', 'abc') = {result}")
    assert result == []

    # Kilka zestawów danych testowych
    result = find_naive("abc", "abcdeabc")
    print(f"find_naive('abc', 'abcdeabc') = {result}")
    assert result == [0, 5]
    
    result = find_naive("abc", "abcabcabc")
    print(f"find_naive('abc', 'abcabcabc') = {result}")
    assert result == [0, 3, 6]
    
    result = find_naive("abc", "ababab")
    print(f"find_naive('abc', 'ababab') = {result}")
    assert result == []
    
    result = find_naive("ab", "ababab")
    print(f"find_naive('ab', 'ababab') = {result}")
    assert result == [0, 2, 4]
    
    print("Naive passed tests")


def test_kmp():
    # Test pustego wzorca
    result = find_kmp("", "abcde")
    print(f"find_kmp('', 'abcde') = {result}")
    assert result == [0, 1, 2, 3, 4, 5]
    
    # Test pustego tekstu
    result = find_kmp("abc", "")
    print(f"find_kmp('abc', '') = {result}")
    assert result == []

    # Test pustego wzorca i tekstu
    result = find_kmp("", "")
    print(f"find_kmp('', '') = {result}")
    assert result == [0]

    # Test wzorca równego tekstowi
    result = find_kmp("abc", "abc")
    print(f"find_kmp('abc', 'abc') = {result}")
    assert result == [0]

    # Test wzorca dłuższego od tekstu
    result = find_kmp("abcdef", "abc")
    print(f"find_kmp('abcdef', 'abc') = {result}")
    assert result == []

    # Test wzorca nie występującego w tekście
    result = find_kmp("xyz", "abc")
    print(f"find_kmp('xyz', 'abc') = {result}")
    assert result == []

    # Kilka zestawów danych testowych
    result = find_kmp("abc", "abcdeabc")
    print(f"find_kmp('abc', 'abcdeabc') = {result}")
    assert result == [0, 5]
    
    result = find_kmp("abc", "abcabcabc")
    print(f"find_kmp('abc', 'abcabcabc') = {result}")
    assert result == [0, 3, 6]
    
    result = find_kmp("abc", "ababab")
    print(f"find_kmp('abc', 'ababab') = {result}")
    assert result == []
    
    result = find_kmp("ab", "ababab")
    print(f"find_kmp('ab', 'ababab') = {result}")
    assert result == [0, 2, 4]
    
    print("KMP passed tests")

def test_kr():
    # Test pustego wzorca
    result = find_karp_rabin("", "abcde")
    print(f"find_karp_rabin('', 'abcde') = {result}")
    assert result == [0, 1, 2, 3, 4, 5]
    
    # Test pustego tekstu
    result = find_karp_rabin("abc", "")
    print(f"find_karp_rabin('abc', '') = {result}")
    assert result == []

    # Test pustego wzorca i tekstu
    result = find_karp_rabin("", "")
    print(f"find_karp_rabin('', '') = {result}")
    assert result == [0]

    # Test wzorca równego tekstowi
    result = find_karp_rabin("abc", "abc")
    print(f"find_karp_rabin('abc', 'abc') = {result}")
    assert result == [0]

    # Test wzorca dłuższego od tekstu
    result = find_karp_rabin("abcdef", "abc")
    print(f"find_karp_rabin('abcdef', 'abc') = {result}")
    assert result == []

    # Test wzorca nie występującego w tekście
    result = find_karp_rabin("xyz", "abc")
    print(f"find_karp_rabin('xyz', 'abc') = {result}")
    assert result == []

    # Kilka zestawów danych testowych
    result = find_karp_rabin("abc", "abcdeabc")
    print(f"find_karp_rabin('abc', 'abcdeabc') = {result}")
    assert result == [0, 5]
    
    result = find_karp_rabin("abc", "abcabcabc")
    print(f"find_karp_rabin('abc', 'abcabcabc') = {result}")
    assert result == [0, 3, 6]
    
    result = find_karp_rabin("abc", "ababab")
    print(f"find_karp_rabin('abc', 'ababab') = {result}")
    assert result == []
    
    result = find_karp_rabin("ab", "ababab")
    print(f"find_karp_rabin('ab', 'ababab') = {result}")
    assert result == [0, 2, 4]
    
    print("KR passed tests")


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
        if karp_rabin_result != naive_result:
            print(f"For input {pattern} in text {text}, expected {naive_result} but got {karp_rabin_result}")
        assert kmp_result == naive_result
        assert karp_rabin_result == naive_result
    
    print("all algorithms have same results for random text and pattern")


if __name__ == "__main__":
    test_naive()
    test_kmp()
    test_kr()
    test_algorithms()
