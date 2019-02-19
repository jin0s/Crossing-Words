from src import crossword

def test_init_Clue():
    clue = crossword.Clue(4,5,6,"D",7)
    assert clue != None
