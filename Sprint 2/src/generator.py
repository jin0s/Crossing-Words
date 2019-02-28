import crossword as cw
import clue_repository as cr
import pandas as pd

class CrosswordGenerator:
    global MAX_CROSSWORD_SIZE
    MAX_CROSSWORD_SIZE = 15
    
    def __init__(self, clue_filename, generate_filepath):
        self.size = MAX_CROSSWORD_SIZE
        self.generate_filepath = generate_filepath
        self.clue_repo = cr.ClueRepository(clue_filename, MAX_CROSSWORD_SIZE)
        self.answers = None
        self.total_generated = 0
        
    def generate(self):
        if not self.clue_repo.is_loaded():
            self.clue_repo.load()
        
        board = CrosswordGenerator.generate_structure(self.size)
        cells, d_ans, a_ans = board.generate_cells_and_answers()
        CrosswordGenerator.generate_answers(cells, d_ans, a_ans)
        CrosswordGenerator.generate_clues(d_ans, a_ans)
#         CrosswordGenerator.to_txt(crossword, self.generate_filepath, self.total_generated)
        self.total_generated += 1
    
    """
    Function to generate the structure, i.e. the position of the black tiles 
    of the board.
    
    Right now just returns a fixed structure 
    """
    def generate_structure(size):
        board = cw.Board(size)
        f = open("sample_structure.txt", "r")
        lines = f.read().split('\n')[:-1]
        for line in lines:
            data = line.split(' ')
            x = int(data[0])
            y = int(data[1])
            num = int(data[2])
            direction = cw.Dir.DOWN if int(data[3]) == 0 else cw.Dir.ACROSS
            length = int(data[4])
            board.set_starting_square(x,y,num,direction, length)
        return board
    
    def generate_answers(cells, d_ans, a_ans):
        return
    
    def generate_clues(d_ans, a_ans):
        return
    
    def to_txt(crossword, filepath, n):    
        file = open(f'{filepath}\\crossword{n}.txt', "w+")
        file.write(str(crossword))
        file.close()
        
