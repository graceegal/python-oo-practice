from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    #TODO: we dont need to hold on to path
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
        self.word_list = [line.strip('\n') for line in file] #strip by default removes any whitespace/new line
        file.close()
        return f"{len(self.word_list)} words read"

    def random(self):
        """ returns a random word from word_list """
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    #TODO: add docstring

    def __init__(self, path):
        """inherits the path from its parent"""
        super().__init__(path)

    def read_path(self):
        """reads file from input and saves words that are not blank or start
        with # as a list to self.word_list. Returns the amount of words read
        """
        file = open(self.path)
        self.word_list = [line.strip("\n") for line in file
                          if not (line.startswith("#") or line.startswith("\n"))]
        file.close()
        return f"{len(self.word_list)} words read"

