'''
Simple testing file to check initialization functionality of crossword.property
'''

from src import crossword

def test_init_Clue():
    clue = crossword.Clue(4,5,6,"D",7)
    assert clue != None

def test_init_Board():
    board = crossword.Board(2)
    assert board != None

def test_init_Crossword():
    cword = crossword.Crossword(2)
    assert cword != None
