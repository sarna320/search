import matplotlib.pyplot as plt


def make_plot(t1, t2, t3, number_words):
    fig, ax = plt.subplots()
    ax.plot(number_words, t1, label="Naive")
    ax.plot(number_words, t2, label="KMP")
    ax.plot(number_words, t3, label="KR")
  
    ax.set_xlabel("Number of words searched")
    ax.set_ylabel("Time [s]")
    ax.legend()
    ax.set_title("Search algorithms")
    plt.savefig("plots/" + "plot" + ".png")
    plt.show()
