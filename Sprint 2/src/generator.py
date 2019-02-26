import crossword as cw
import clue_repository as cr
import pandas as pd

class CrosswordGenerator:
    global MAX_CROSSWORD_SIZE
    MAX_CROSSWORD_SIZE = 15
    
    def __init__(self, _clue_filename, _generate_filepath):
        self.size = MAX_CROSSWORD_SIZE
        self.generate_filepath = _generate_filepath
        self.clue_repo = cr.ClueRepository(_clue_filename, MAX_CROSSWORD_SIZE)
        self.answers = None
        self.total_generated = 0
        
    def generate(self):
        if not clue_repo.is_loaded():
            self.clue_repo.load()
        crossword = cw.Crossword(self.size)
        CrosswordGenerator.generate_structure(crossword)
        CrosswordGenerator.generate_clue_set(crossword)
        CrosswordGenerator.to_txt(crossword, self.generate_filepath, self.total_generated)
        self.total_generated += 1
    
    def generate_structure(crossword):
        return 
    
    def generate_clue_set(crossword):
        return
    
    def to_txt(crossword, filepath, n):    
        file = open(f'{filepath}\\crossword{n}.txt', "w+")
        file.write(str(crossword))
        file.close()
