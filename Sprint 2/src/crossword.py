import numpy as np
from enum import Enum
#====================================================================================
class Dir(Enum):
    DOWN = 0
    ACROSS = 1
#====================================================================================
"""
Class to store the clue/answer pair
Main function is to simplify crossword printing 
by being able to print the answer object and clue on the same line

Allows for setting of clues after initialization
"""
class Clue:
    
    def __init__(self, answer):
        self.answer = answer
        self.clue = ""
    
    def __init__(self, answer, clue):
        self.answer = answer
        self.clue = clue
        
    def set_clue(self, clue):
        self.clue = clue
    
    """
    Function to print the Clue in the format:
    {"d":direction, "n":number, "x":x_position, "y":y_position, "a":answer, "c":clue}
    length is implicit and therefore unincluded
    """
    def __str__(self):
        d = "down" if self.answer.direction == Dir.DOWN else "across"
        n = self.answer.number
        x = self.answer.x_position
        y = self.answer.y_position
        a = self.answer.get_answer()
        c = self.clue
        return f'{{"d":"{d}", "n":{n}, "x":{x}, "y":{y}, "a":"{a}", "c":"{c} }}"'
    
#====================================================================================

"""
Class that stores a single position on the crossword
Stores a modifiable letter and a pointer to the across and down word it belongs to
"""
class Cell:
    
    def __init__(self, x_position, y_position, across_answer, down_answer):
        self.x_position = x_position
        self.y_position = y_position
        self.down_answer = down_answer
        self.across_answer = across_answer
        self.letter = '-'
    
    def set_letter(self, letter):
        self.letter = letter
    
    """
    Function that returns the string form of both the across answer
    and the down answer that this cell belongs to
    """
    def get_answers(self):
        return (self.across_answer.get_answer(), self.down_answer.get_answer())

#====================================================================================
"""
Class to store various metadata about each answer, such as its start position,
length, which direction it is in, and its number for the clue list.

Each Answer is made up of modifiable Cells, belonging to the row of the answer or the 
column of the answer, depending on direction.
"""
class Answer:
    
    def __init__(self, x_position, y_position, length, direction, number):
        #the cell at (x_position, y_position) is the start of the answer
        self.x_position = x_position
        self.y_position = y_position
        
        self.direction = direction
        
        self.length = length
        
        self.cells = [None for i in range(0, length)]
    
    """
    Function to add cells to the object
    
    Cells must be added after the initialization of the object due to the
    fact that they can be shared between different answers.
    """
    def add_cell(self, cell):
        if self.direction == Dir.ACROSS:
            assert(cell.x_position == self.x_position)
            index = cell.y_position - self.y_position
        elif self.direction == Dir.DOWN:
            assert(cell.y_position == self.y_position)
            index = cell.x_position - self.x_position
        
        #cell is not valid if is behind or above the initial cell of the answer
        assert(index >= 0)
        
        #cells are modifiable and therefore should not be replaced
        assert(self.cells[index] is None)
        
        self.cells[index] = cell
    
    """
    Function for adding multiple cells at a time
    """
    def add_cells(self, cells):
        for cell in cells:
            self.add_cell(cell)
    
    """
    Function that returns the string form of the answer
    if cells are unmarked or uninitialized they will be represented as '-'
    """
    def get_answer(self):
        answer = ""
        for cell in self.cells:
            answer += '-' if cell is None else cell.letter
        return answer
    
#====================================================================================

class Board:
    global MAX_ANSWERS
    MAX_ANSWERS = 80
    
    def __init__(self, sz):
        self.size = sz
        self.start_board = np.zeros((sz,sz))
        self.down_board = np.zeros((sz,sz))
        self.across_board = np.zeros((sz,sz))
        self.across_length = np.zeros(MAX_ANSWERS+1)
        self.down_length = np.zeros(MAX_ANSWERS+1)
    
    def set_empty_square(self, x, y):
        self.start_board[x][y] = -1
    
    def set_starting_square(self, x, y, number, direction, length):
        assert(self.start_board[x][y] == 0 or self.start_board[x][y] == number)
        self.start_board[x][y] = number
        
        #The answer cannot be interrupted by empty tiles
        if direction == Dir.DOWN:
            down_length[number] = length
            for nx in range(x, x+length):
                down_board[nx][y] = number
                assert(self.start_board[nx][y] != -1)
        else:
            across_length[number] = length
            for nx in range(y, y+length):
                across_board[x][ny] = number
                assert(self.start_board[x][ny] != -1)
        
        #The end of an answer must always be an empty square
        nx = x + (0 if direction == Dir.ACROSS else length)
        ny = y + (0 if direction == Dir.DOWN else length)
        self.set_empty_square(nx, ny)
        
"""    
    def generate_cell_metadata(self):
        metadata = []
        for x in range(0, self.size):
            for y in range(0, self.size):
                #Ignore cells that are empty
                if start_board[x][y] != -1:
                    metadata.append((x,y,down_board[x][y], across_board[x][y]))
        return metadata
    
    def generate_answer_metadata():
        metadata = []
        for x in range(0, self.size):
            for y in range(0, self.size):
                #Ignore cells that aren't the start of a word
                if start_board[x][y] > 0:
     
                    #Append the down word data if it exists
                    if down_length[start_board[x][y]] > 0:
                        metadata.append((start_board[x][y], x,y, Dir.DOWN, down_length[start_board[x][y]]))
                    
                    #Append the across word data if it exists
                    if across_length[start_board[x][y]] > 0:
                        metadata.append((start_board[x][y], x,y, Dir.DOWN, down_length[start_board[x][y]]))
        return metadata
"""

    
#====================================================================================    
    
class Crossword: 
    
    def __init__(self, size, board):
        self.size = size
        self.board = board
        self.clues = []
    
    def __str__(self):
        return  f'{{\n"title": "Randomly Generated Crossword",\n"by": "#1 POOSD Group",\n"clues":{self.clues}\n}}'
    
