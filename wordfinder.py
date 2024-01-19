"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Read in words from a file, do stuff with them"""
    def __init__(self, file_path):
        self.count = 0
        file = open(file_path, "r")
        self.words = self.read(file)
        print(f"{self.count} words read")
        file.close()

    def read(self, file):
        """Read in from file line by line, strip newlines and spaces"""
        obj = []
        for line in file:
            obj.append(line.strip())
            self.count += 1
        return obj

    def random(self):
        """Return a random word from the list of words read in"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """remove blank lines and #s"""
    def read(self, file):
        obj = []
        for line in file:
            line = line.strip()
            if (line.find("#") == -1) and (line):
                obj.append(line)
                self.count += 1
        return obj        