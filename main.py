import file, KMP, KR, N, time, plot


def main():
    # Lists to store execution times
    times_KMP = []
    times_N = []
    times_KR = []

    # Number of words to search in each iteration
    number_of_words = list(range(100, 1100, 100))

    # Load all words from the text file
    path = "pan-tadeusz.txt"
    all_words = file.load_file(path, -1)
    # print(all_words)

    for num in number_of_words:
        print(num)
        # Load a specified number of words from the text file
        words = file.load_file(path, num)
        # print(words)

        # Measure the execution time of the KMP algorithm
        start = time.process_time()
        for word in words:
            KMP.find_kmp(word, all_words)
        stop = time.process_time()
        times_KMP.append(stop - start)
        print("KMP done")

        # Measure the execution time of the Karp-Rabin algorithm
        start = time.process_time()
        for word in words:
            KR.find_karp_rabin(word, all_words)
        stop = time.process_time()
        times_KR.append(stop - start)
        print("KR done")

        # Measure the execution time of the Naive algorithm
        start = time.process_time()
        for word in words:
            N.find_naive(word, all_words)
        stop = time.process_time()
        times_N.append(stop - start)
        print("Naive done")

    # Generate and display a plot based on the recorded execution times
    plot.make_plot(times_N, times_KMP, times_KR, number_of_words)


if __name__ == "__main__":
    main()



