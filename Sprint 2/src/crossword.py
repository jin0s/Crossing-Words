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
        d = "Down" if self.answer.direction == Dir.DOWN else "Across"
        n = self.answer.number
        x = self.answer.x_position
        y = self.answer.y_position
        a = self.answer.get_answer()
        c = self.clue
        return f'{{"direction":"{d}", "number":{n}, "x":{x}, "y":{y}, "answer":"{a}", "hint":"{c}"}}'
    
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
    
    def __str__(self):
        return self.letter
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.x_position == other.x_position and self.y_position == other.y_position
    
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
        self.number = number
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
            answer += str(cell)
        return answer
    
    def __str__(self):
        d = "down" if self.direction == Dir.DOWN else "across"
        n = self.number
        x = self.x_position
        y = self.y_position
        a = self.get_answer()
        return f'"d":"{d}", "n":{n}, "x":{x}, "y":{y}, "a":"{a}"'
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.x_position == other.x_position and self.y_position == other.y_position
    
    
#====================================================================================

class Board:
    global MAX_ANSWERS
    MAX_ANSWERS = 120
    
    def __init__(self, sz):
        self.size = sz
        self.start_board = np.zeros((sz,sz), dtype=np.int32)
        self.down_board = np.zeros((sz,sz), dtype=np.int32)
        self.across_board = np.zeros((sz,sz), dtype=np.int32)
        self.across_length = np.zeros(MAX_ANSWERS+1, dtype=np.int32)
        self.down_length = np.zeros(MAX_ANSWERS+1, dtype=np.int32)
    
    """
    Function to set a square as a black tile on the board
    """
    def set_empty_square(self, x, y):
        assert(self.start_board[x][y] == 0 or self.start_board[x][y] == -1)
        self.start_board[x][y] = -1
    
    """
    Function to set a square as the start of either a down or 
    an across answer. 
    """
    def set_starting_square(self, x, y, number, direction, length):
        assert(self.start_board[x][y] == 0 or self.start_board[x][y] == number)
        self.start_board[x][y] = number
        
        #The answer cannot be interrupted by empty tiles
        if direction == Dir.DOWN:
            self.down_length[number] = length
            for nx in range(x, x+length):
                self.down_board[nx][y] = number
                assert(self.start_board[nx][y] != -1)
        else:
            self.across_length[number] = length
            for ny in range(y, y+length):
                self.across_board[x][ny] = number
                assert(self.start_board[x][ny] != -1)
        
        #The end of an answer must always be an empty square or the end of the board
        nx = x + (0 if direction == Dir.ACROSS else length)
        ny = y + (0 if direction == Dir.DOWN else length)
        if nx < self.size and ny < self.size:
            self.set_empty_square(nx, ny)
    
    """
    Function that returns the cell and answer set for a crossword
    with complete structure
    
    Crossword must be checked and valid
    """
    def generate_cells_and_answers(self):
        #initialize everything to None
        down_answers, across_answers = self.initialize_answers()
        cells = self.initialize_cells(down_answers, across_answers)
        return (cells, down_answers, across_answers)
    
    """
    Function that initializes the Answer objects of the board
    
    Returns a tuple of the (down_answers, across_answers)
    """
    def initialize_answers(self):
        down_answers = [None] * MAX_ANSWERS
        across_answers = [None] * MAX_ANSWERS
        
        #intialize all answers by iterating through the startboard
        for x in range(0, self.size):
            for y in range(0, self.size):
                #Ignore cells that aren't the start of a word
                if self.start_board[x][y] == 0 or self.start_board[x][y] == -1:
                    continue
                
                #aid is the answer id
                aid = self.start_board[x][y]

                #Add the down answer if it exists
                if self.down_length[aid] > 0:
                    down_answers[aid] = Answer(x,y,self.down_length[aid],Dir.DOWN, aid)

                #Add the across answer if it exists
                if self.across_length[aid] > 0:
                    across_answers[aid] = Answer(x,y,self.across_length[aid], Dir.ACROSS, aid)

        #end initialization
        return (down_answers, across_answers)
    
    """
    Function that initializes the Cell objects of the board
    
    Requires the list of down and across answers for the board
    Returns a 2-D array of every cell in the crossword, with cells that
    are empty represented as None
    """
    def initialize_cells(self, down_answers, across_answers):
        cells = [[None]*self.size for i in range(0, self.size)]
        
        for x in range(0, self.size):
            for y in range(0, self.size):
                #Ignore cells that are empty
                if self.start_board[x][y] == -1:
                    continue
                
                #instantiate the cell with pointers to the answer it belongs to
                across_answer = across_answers[self.across_board[x][y]]
                down_answer = down_answers[self.down_board[x][y]]
                cells[x][y] = Cell(x,y,across_answer, down_answer)
                
                #add the cell to the answers it belongs to
                across_answer.add_cell(cells[x][y])
                down_answer.add_cell(cells[x][y])

        return cells
    """
    Function to print out the board
    """
    def __str__(self):
        return str(self.start_board)
#====================================================================================    
    
class Crossword: 
    
    def __init__(self, size):
        self.size = size
        self.clues = []
    
    def add_clue(self, answer, clue):
        self.clues.append(Clue(answer, clue))
        
    def __str__(self):
        clue_str = "["
        for clue in self.clues:
            clue_str += str(clue) + ","
        clue_str = clue_str[:-1] +"]"
        return  f'{{\n"title": "Randomly Generated Crossword",\n"by": "#1 POOSD Group",\n"clues":{clue_str}\n}}'
    
