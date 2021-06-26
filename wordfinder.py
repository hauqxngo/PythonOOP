"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Find random words from dictionary.
    
    >>> wf = WordFinder("pets.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "fish"]
    True

    >>> wf.random() in ["cat", "dog", "fish"]
    True

    >>> wf.random() in ["cat", "dog", "fish"]
    True
    """

    def __init__(self, path):
        """Read dictionary and states number of words read."""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_fiile to lists of words."""
        return [word.strip() for word in dict_file]

    def random(self):
        """Return random word."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WprdFinder that excludes blank lines/comments.
    >>> swf = SpecialWordFinder("goodforyou.txt")
    4 words read

    >>> swf.random() in ["kale", "spinach", "apple", "banana"]
    True

    >>> swf.random() in ["kale", "spinach", "apple", "banana"]
    True

    >>> swf.random() in ["kale", "spinach", "apple", "banana"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file to list of words, but skip blanks/comments."""

        return [word.strip() for word in dict_file
                if word.strip() and not word.startswith("#")]
