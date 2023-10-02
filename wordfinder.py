"""Word Finder: finds random words from a dictionary."""
import random 
path = "C:\Users\iankm\.vscode\python-oo-practice\words.txt"


class WordFinder(): 

    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def __repr__(self):
        return "More Detail!"

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)
    

class SpecialWordFinder():

    def parse(self, dict_file):

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]