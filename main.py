import file, KMP, KR, N, time, plot


def main():
    times_KMP = []
    times_N = []
    times_KR = []

    number_of_words = list(range(10, 50, 10))
    path = "pan-tadeusz.txt"
    all_words = file.load_file(path, -1)
    for num in number_of_words:
        print(num)
        words = file.load_file(path, num)

        start = time.process_time()
        for word in words:
            KMP.find_kmp(word, all_words)
        stop = time.process_time()
        times_KMP.append(stop - start)
        print("KMP done")

        start = time.process_time()
        for word in words:
            KR.find_karp_rabin(word, all_words)
            continue
        stop = time.process_time()
        times_KR.append(stop - start)
        print("KR done")

        start = time.process_time()
        for word in words:
            N.find_naive(word, all_words)
        stop = time.process_time()
        times_N.append(stop - start)
        print("Naive done")
    plot.make_plot(times_N, times_KMP, times_KR, number_of_words)


if __name__ == "__main__":
    main()
