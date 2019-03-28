'''
Unit test for adding answers and cells onto the board. It then checks to see if
each answers have the correct down and across answers
'''

from src.crossword import *

def test_cells_and_answer_class():
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
   assert(d_ans[0].get_answer() == "AC")
   assert(d_ans[1].get_answer() == "BD")
   assert(a_ans[0].get_answer() == "AB")
   assert(a_ans[1].get_answer() == "CD")
