from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """ Creates a word finder from given path
        Reads file from input path and saves it to word_list"""
        self.path = path
        self.word_list = []

        self.read_path()

    def __repr__(self):
        return f"word finder from path {self.path}"

    def read_path(self):
        """ reads file from input and saves words as a list to self.word_list
        returns the amount of words read """
        file = open(self.path)
        self.word_list = [line.strip('\n') for line in file]
        # for line in file:
        #     self.word_list.append(line)
        file.close()
        return f"{len(self.word_list)} words read"

    def random(self):
        """ returns a random word from word_list """
        return choice(self.word_list)


