import matplotlib.pyplot as plt


def make_plot(t1, t2, t3, number_words):
    # Create a figure and an axes
    fig, ax = plt.subplots()

    # Plotting the data for each search algorithm
    ax.plot(number_words, t1, label="Naive")
    ax.plot(number_words, t2, label="KMP")
    ax.plot(number_words, t3, label="KR")

    # Setting labels and title for clarity
    ax.set_xlabel("Number of words searched")
    ax.set_ylabel("Time [s]")
    ax.set_title("Search algorithms")

    # Display the legend to identify each line plot
    ax.legend()

    plt.savefig("plots/plot.png")
    plt.show()
