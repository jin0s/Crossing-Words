'''
Unit test to check generator.py functions
'''

from src import generator
from src import crossword

gen = generator.CrosswordGenerator(1, "../Data/clues.csv", "./")
cword = crossword.Crossword(1);


def test_generate_structure():
    gen.generate_structure()

def test_generate_clue_set():
    gen.generate_clue_set()

def load_clues():
    gen.load_clues()

def test_generate_trie():
    gen.generate_trie()
