'''
Simple testing file to check initialization functionality of crossword.py
'''
from src.crossword import *
from src.clue_repository import *
from src.generator import *
"""
Unit Tests for the Clue, Cell, Answer, Board, and Crossword classes
Classes are very interwoven, so a lot of code is reused.
Many functions are tested implicitly by other unit tests
"""
"""
Unit tests for Clue class
"""
def test_init_clue():
    l = 2
    d_ans = [None]*l
    a_ans = [None]*l
    cells = [[None]*l for i in range(0, l)]

    for i in range(0, l):
        d_ans[i] = Answer(0,i,l,Dir.DOWN,i)
        a_ans[i] = Answer(i,0,l,Dir.ACROSS,i)

    for row in range(0,l):
        for col in range(0,l):
            let = chr(ord('A')+(row*l)+col)
            cells[row][col] = Cell(row, col, a_ans[row], d_ans[col])
            a_ans[row].add_cell(cells[row][col])
            d_ans[col].add_cell(cells[row][col])
            cells[row][col].set_letter(let)
    clue = Clue(d_ans[i], "AA")
    assert(clue is not None)

def test_set_clue_clue():
    l = 2
    d_ans = [None]*l
    a_ans = [None]*l
    cells = [[None]*l for i in range(0, l)]

    for i in range(0, l):
        d_ans[i] = Answer(0,i,l,Dir.DOWN,i)
        a_ans[i] = Answer(i,0,l,Dir.ACROSS,i)

    for row in range(0,l):
        for col in range(0,l):
            let = chr(ord('A')+(row*l)+col)
            cells[row][col] = Cell(row, col, a_ans[row], d_ans[col])
            a_ans[row].add_cell(cells[row][col])
            d_ans[col].add_cell(cells[row][col])
            cells[row][col].set_letter(let)
    clue = Clue(d_ans[i], "AA")
    clue.set_clue("AB")
    assert(clue.clue =="AB")

"""
Unit tests for Cell class
"""
def test_init_cell():
    l = 2
    d_ans = [None]*l
    a_ans = [None]*l
    cells = [[None]*l for i in range(0, l)]

    for i in range(0, l):
        d_ans[i] = Answer(0,i,l,Dir.DOWN,i)
        a_ans[i] = Answer(i,0,l,Dir.ACROSS,i)

    for row in range(0,l):
        for col in range(0,l):
            let = chr(ord('A')+(row*l)+col)
            cells[row][col] = Cell(row, col, a_ans[row], d_ans[col])
            a_ans[row].add_cell(cells[row][col])
            d_ans[col].add_cell(cells[row][col])
            cells[row][col].set_letter(let)
    board_flat = ""
    for i in range(0,l):
        for j in range(0,l):
            board_flat += str(cells[i][j])
    assert(board_flat == "ABCD")

def test_set_letter_cell():
    l = 2
    d_ans = [None]*l
    a_ans = [None]*l
    cells = [[None]*l for i in range(0, l)]

    for i in range(0, l):
        d_ans[i] = Answer(0,i,l,Dir.DOWN,i)
        a_ans[i] = Answer(i,0,l,Dir.ACROSS,i)

    for row in range(0,l):
        for col in range(0,l):
            let = chr(ord('A')+(row*l)+col)
            cells[row][col] = Cell(row, col, a_ans[row], d_ans[col])
            a_ans[row].add_cell(cells[row][col])
            d_ans[col].add_cell(cells[row][col])
            cells[row][col].set_letter(let)
    cells[0][0].set_letter("V")
    assert(cells[0][0].letter == 'V')

"""
Unit tests for answer class
the init is tested implicitly in every function in this section
"""
def test_get_answer_answer():
    l = 2
    d_ans = [None]*l
    a_ans = [None]*l
    cells = [[None]*l for i in range(0, l)]

    for i in range(0, l):
        d_ans[i] = Answer(0,i,l,Dir.DOWN,i)
        a_ans[i] = Answer(i,0,l,Dir.ACROSS,i)

    for row in range(0,l):
        for col in range(0,l):
            let = chr(ord('A')+(row*l)+col)
            cells[row][col] = Cell(row, col, a_ans[row], d_ans[col])
            a_ans[row].add_cell(cells[row][col])
            d_ans[col].add_cell(cells[row][col])
            cells[row][col].set_letter(let)
    assert(d_ans[0].get_answer() == "AC")
    assert(d_ans[1].get_answer() == "BD")
    assert(a_ans[0].get_answer() == "AB")
    assert(a_ans[1].get_answer() == "CD")
    
"""
Unit tests for Board class
the init is tested implicitly in every function in this section
The Board class is still a work in progress and largely unused at this point in the Project
"""
def test_starting_square():
    board = Board(3)

    board.set_starting_square(0,0,1,Dir.DOWN,3)
    board.set_starting_square(0,1,2,Dir.DOWN,3)
    board.set_starting_square(0,2,3,Dir.DOWN,2)

    board.set_starting_square(0,0,1,Dir.ACROSS,3)
    board.set_starting_square(1,0,4,Dir.ACROSS,3)
    board.set_starting_square(2,0,5,Dir.ACROSS,2)
    
    assert(board.start_board[0][0] == 1)
def test_generate_cells_and_answers_board():
    board = Board(3)

    board.set_starting_square(0,0,1,Dir.DOWN,3)
    board.set_starting_square(0,1,2,Dir.DOWN,3)
    board.set_starting_square(0,2,3,Dir.DOWN,2)

    board.set_starting_square(0,0,1,Dir.ACROSS,3)
    board.set_starting_square(1,0,4,Dir.ACROSS,3)
    board.set_starting_square(2,0,5,Dir.ACROSS,2)
    
    assert(board.generate_cells_and_answers() is not None)
