from src import generator
from src import crossword

gen = generator.CrosswordGenerator(1, "../clues.csv", "./")
cword = crossword.Crossword(1);


def test_generate_structure():
    gen.generate_structure()


def test_generate_clue_set():
    gen.generate_clue_set()


def test_generate_trie():
    gen.generate_trie()

def test_load_clues():
    gen.load_clues()
