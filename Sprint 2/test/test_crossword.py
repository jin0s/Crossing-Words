'''
Simple testing file to check initialization functionality of crossword.property
'''

from src import crossword

clue = crossword.Clue(4,5,6,"D",7)
print(clue)

def test_init_Clue():
    assert clue != None

# Simple check to see if the __str__ is returning properly
def test__str__():
    retval = str(clue)
    assert retval == retval

def test_init_Board():
    board = crossword.Board(2)
    assert board != None

def test_init_Crossword():
    cword = crossword.Crossword(2)
    assert cword != None
