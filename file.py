import unidecode
import re


def load_file(path, n):
    # Open a text file for reading in UTF-8 encoding
    with open(path, "r", encoding="utf8") as file:
        # Read the entire content of the file
        data = file.read()

    # Convert the text to lowercase to maintain consistency
    data = data.lower()

    # Remove any accents from characters and normalize them
    data = unidecode.unidecode(data)

    # If n is -1, process the text as a single string containing all words
    if n == -1:
        # Split the data into words using regex, filtering out non-alphabetical characters
        list_of_words = re.split("[^a-z]+", data)
        # Join words into a single string, excluding words with less than 2 characters
        list_of_words = " ".join([word for word in list_of_words if len(word) >= 2])

    # If n is a positive number, process only the first 'n' words
    if n > 0:
        # Split the data into words, limiting the number of splits to 'n'
        list_of_words = re.split("[^a-z]+", data, n)
        # Remove the last element from the list as it's the part of the text after the nth word
        list_of_words.pop()
        # Filter out words with less than 3 characters
        list_of_words = [word for word in list_of_words if len(word) >= 2]

    # Return the processed list of words
    return list_of_words
