'''
Simple testing file to check initialization functionality of crossword.py
'''

from src import crossword

def test_init_Board():
    board = crossword.Board(15)
    assert board != None

def test_init_Crossword():
    board = crossword.Board(15)
    cword = crossword.Crossword(15, board)
    assert cword != None

def test_init_Answer():
    answer = crossword.Answer(1,2,5,"Across",5)
    assert answer != None

def test_init_Clue():
    answer = crossword.Answer(1,2,5,"Across",5)
    clue = crossword.Clue(answer)
    assert clue != None

def test_init_Cell():
    cell = crossword.Cell(1, 2, "Across", "Down")
    assert cell != None
