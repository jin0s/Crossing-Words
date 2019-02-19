import numpy as np

class Clue:
    
    def __init__(self, x_pos, y_pos, num, _direction, _length):
        self.x_position = x_pos
        self.y_position = y_pos
        self.number = num
        self.direction = _direction
        self.length = _length
        self.clue = ""
        self.answer = np.ndarray(self.length, dtype='<U1')
        self.answer[:] = 'a'
        self.index = -1
    
    def arr_to_string(arr):
        return "".join(str(a) for a in arr)
    
    def __str__(self):
        return f'{{d":"{self.direction}", "n":{self.number}, "x":{self.x_position}, "y":{self.y_position}, "a":"{clue.arr_to_string(self.answer)}", "c":"{self.clue} }}"'

class Board:
    
    def __init__(self, sz):
        self.size = sz
        self.start_board = np.zeros((sz,sz))
        self.letter_board = np.zeros((sz,sz), dtype='>U1')
        
class Crossword: 
    
    def __init__(self, sz):
        self.size = sz
        self.board = Board(self.size)
        self.clues = []
    
    def __str__(self):
        return  f'{{\n"title": "Randomly Generated Crossword",\n"by": "#1 POOSD Group",\n"clues":{self.clues}\n}}' 

