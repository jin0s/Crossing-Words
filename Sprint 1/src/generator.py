from src import crossword as cw
from src import trie
import pandas as pd

class CrosswordGenerator:
    global MAX_CROSSWORD_SIZE
    MAX_CROSSWORD_SIZE = 15
    def __init__(self, clue_filename_, generate_filepath_):
        self.size = MAX_CROSSWORD_SIZE
        self.clue_filename = clue_filename_
        self.generate_filepath = generate_filepath_
        self.clue_repo = None
        self.answers = None
        self.total_generated = 0

    def generate(self):
        if self.clue_repo is None:
            self.load_clues()
        if self.answers is None:
            self.generate_trie()
        crossword = cw.Crossword(self.size)
        CrosswordGenerator.generate_structure(crossword)
        CrosswordGenerator.generate_clue_set(crossword)
        CrosswordGenerator.to_txt(crossword, self.generate_filepath, self.total_generated)
        self.total_generated += 1

    def generate_structure(crossword):
        return

    def generate_clue_set(crossword):
        return

    def to_txt(crossword, filepath, n):
        file = open(f'{filepath}\\crossword{n}.txt', "w+")
        file.write(str(crossword))
        file.close()

    def load_clues(self):
        self.clue_repo = pd.read_csv(self.clue_filename)
        self.clue_repo.dropna()
        self.generate_trie()

    def generate_trie(self):
        self.answers = trie.Trie()
        unique = self.clue_repo.drop_duplicates('answer')['answer'].values
        for word in unique:
            self.answers.insert_word(word)
