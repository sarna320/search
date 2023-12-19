# Piotr Niedziałek
import unidecode
import re


def load_file(path, n):
    with open(
        path,
        "r",
        encoding="utf8",  # there was a problem, without "utf8", would not work
    ) as file:  # opening file from your working folder
        data = file.read()
    data = data.lower()
    # print(data)
    data = unidecode.unidecode(data)

    if n == -1:
        return data
    if n > 0:
        list_of_words = re.split("[^a-z]+", data, n)
        list_of_words.pop()  # we delete rest of words that we do not need

    return list_of_words
