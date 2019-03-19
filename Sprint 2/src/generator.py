import crossword as cw
import clue_repository as cr
import pandas as pd
import numpy as np
from timeit import default_timer as timer 


class CrosswordGenerator:
    #Fix the max crossword size 
    global MAX_CROSSWORD_SIZE
    MAX_CROSSWORD_SIZE = 15
    
    def __init__(self, clue_filename, generate_filepath):
        self.size = MAX_CROSSWORD_SIZE
        self.generate_filepath = generate_filepath
        self.clue_repo = cr.ClueRepository(clue_filename, MAX_CROSSWORD_SIZE)
        self.answers = None
        self.total_generated = 0
    
    """
    Function to randomly generate a crossword
    """
    def generate(self):
        #load the clue repository
        if not self.clue_repo.is_loaded():
            self.clue_repo.load()
        
        #generate the structure of the board
        board = self.generate_structure()
        
        #Generate the cell and answer objects for the backtrackings
        cells, d_ans, a_ans = board.generate_cells_and_answers()
        
        #generate the answers via backtracking
        self.generate_answers(cells)
        
        #randomly select clues to fit each answer
        crossword = self.generate_clues(d_ans, a_ans)
        
        #Crossword will be returned as None if it is invalid
        if crossword is None:
            self.generate()
            return
        
        #Print the crossword to the file
        CrosswordGenerator.to_txt(crossword, self.generate_filepath, self.total_generated)
        self.total_generated += 1
    
    """
    Function to generate the structure, i.e. the position of the black tiles 
    of the board.
    
    Right now just returns a fixed structure 
    """
    def generate_structure(self):
        #initialize the board
        board = cw.Board(self.size)
        
        #This is placeholder code, just reads in a specification for structure 
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
    
    """
    Function to populate the board with letters
    
    Uses a backtracking method via the backtrack() function,
    the backtracking follows the order set in the find_ordering() function
    """ 
    def generate_answers(self, cells):
        #find a heuristically optimal order for the backtracking to follow
        self.order = self.find_ordering(cells)
        
        #set each cell in its corresponding index
        #this allows the backtracking to be more straightforward
        indices = [None]*200
        for x in range(0, self.size):
            for y in range(0, self.size):
                indices[self.order[x][y]] = cells[x][y]
        
        #call the recursive backtracking function
        self.backtrack(0,indices, cells)
        
        #print the cells to the console upon successful run
        CrosswordGenerator.print_cells(cells)
        return
    
    """
    Function to set the order of the backtracking
    
    The priority is Right, Left, Up, Down:
    any cells found to the Right of previous cells
    will be processed before cells found to the Left, etc.
    
    EX:
    1  2  3  █ 10 11
    4  5  6  7  8  9
    █  █  █  █  █ 12
    """
    def find_ordering(self, cells):
        #Set the direction vectors
        #index corresponds to the priority of each vector
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        
        #Initialize the queues for the 0-K bfs
        order = np.zeros((self.size, self.size), dtype=np.int32)-1
        queues = [[] for i in range(0,4)]
        queues[0].append((0,0))
        index = 0
        
        #BFS can end seemingly arbitrarily
        while True:
            
            # find the x,y coordinates with the highest priority
            x = -1
            y = -1
            for d in range(0,4):
                if queues[d]:
                    x,y = queues[d].pop()
                    break
            
            # if none found, the bfs is finished
            if x == -1:
                break
            
            # if the cell is already processed, ignore it
            if order[x][y] != -1:
                continue
            
            # set the index of the cell
            order[x][y] = index
            index += 1
            
            # look in the four directions, adding cells to the queue with their
            #respective priority
            for d in range(0,4):
                nx = x + dx[d]
                ny = y + dy[d]
                #check to ensure the cell is in bounds, not processed, and not a wall
                if(nx < self.size and nx >= 0 
                   and ny < self.size and ny >= 0 
                   and order[nx][ny]==-1 
                   and cells[nx][ny] is not None):
                    queues[d].insert(0, (nx,ny))
        #Ordering completed
        return order
     
        
    """
     Recursive backtracking function to find the answers
     
     returns a tuple of a boolean, indicating if the backtracking is finished,
     and a cell to backtrack to if not
    """
    def backtrack(self, ind, cells, pc):
        #BASE CASE: we've run out of cells to process,
        #Every cell should be set
        if cells[ind] == None:
            return (None, True)

        #Backtracking aid:
        #If we've already placed this cell, it means that its solution is more likely to succeed
        first_attempt = False
        if cells[ind].letter != '-':
            first_attempt = True

        #keep track of which letters have been tried
        tried = np.ones(26)
        while tried.any():
            #attempt to place a cell
            if( not first_attempt): # if there is an original letter, leave it in place
                #function that places a cell
                can = self.place_cell(cells[ind], tried) 
                if not can[1]:
                    #We can not place a cell here, three reasons why:
                    
                    # 1. board is entirely invalid
                    if can[0] == None:
                        #hard reset the board
                        return (None, False)
                    
                    # 2. board is invalid because of letters left in place
                    #remove them and try again
                    c_ord = self.order[can[0].x_position][can[0].y_position] 
                    if c_ord > ind:
                        cells[c_ord].set_letter('-')
                        tried[ord(cells[ind].letter)-ord('A')] = 0
                        continue
                    
                    # 3. board is invalid because of something before us
                    #backtrack to find it
                    return (can[0], False)
            #original cell letter can only be used once    
            first_attempt = False
            
            #debug print output
            global places
            places += 1
            if(places % 10000 == 0):
                CrosswordGenerator.print_cells(pc)
                print()
            
            # pursue the solution with the current cell set
            result = self.backtrack(ind+1, cells, pc)
            if result[1]: 
                # it worked!
                return (None, True)
            elif result[0] == None:
                # it didn't work, and no solutions exist
                #return to the 0th cell
                if(ind == 0):
                    continue
                else:
                    return (None, False)
            elif result[0] != cells[ind]:
                # it didn't work, but not because of this cell
                
                # 2 options:
                c_ord = self.order[result[0].x_position][result[0].y_position] 
                if c_ord > ind:
                    # 1.  it didnt work because of a letter after this cell left set
                    # reset the letter
                    cells[c_ord].set_letter('-')
                    tried[ord(cells[ind].letter)-ord('A')] = 0
                    continue
                
                # 2. it didnt work because of a letter before this cell
                #backtrack to find it
                #can leave this cell set iff it is not part of the same answer as the cell in question
                if(result[0].down_answer == cells[ind].down_answer or 
                     result[0].across_answer == cells[ind].across_answer):
                    # clear out everything in the answers
                    cells[ind].set_letter('-')
                return(result[0], False)
            
            #it didnt work, because of this cell
            #try a different letter, but remove this letter from the possible letters
            tried[ord(cells[ind].letter)-ord('A')] = 0
        
        #nothing in this cell worked
        #return to the previous cell in this answer
        cells[ind].set_letter('-')
        cell_return = self.find_last_active_cell(cells[ind].across_answer, cells[ind])[1]
        if cell_return is None:
            cell_return = self.find_last_active_cell(cells[ind].down_answer, cells[ind])[1]
        return (cell_return, False)
    
    """
    function to find the last active cell within a certain answer
    
    for utility, will also return the index of the cell inputted
    """
    def find_last_active_cell(self, answer, cell):
        last_cell = None
        last_cell_ind = -1
        c_index = -1
        # iterate through the cells in the answer
        for index in range(0, answer.length):
            if answer.cells[index] == cell:
                #this is the input cell
                #save the index
                c_index = index
            
            elif answer.cells[index].letter != '-':
                #this isn't the input cell
                #check to see if its order is higher than current max
                c_x = answer.cells[index].x_position
                c_y = answer.cells[index].y_position
                if(self.order[c_x][c_y] > last_cell_ind):
                    last_cell = answer.cells[index]
                    last_cell_ind = self.order[c_x][c_y]
        return (c_index, last_cell)
    
    """
    Function to place a letter in a cell
    
    Probability any letter will be picked is based on the frequency
    of the letter occuring in a word at the relevant index
    """
    def place_cell(self, cell, tried):
        #find last active cells
        d_index, last_down_cell = self.find_last_active_cell(cell.down_answer, cell)
        a_index, last_across_cell = self.find_last_active_cell(cell.across_answer, cell)
        
        #calculate a weighted frequency
        d_freq = np.array(self.clue_repo.get_frequency(d_index))
        a_freq = np.array(self.clue_repo.get_frequency(a_index))
        d_freq = d_freq/np.sum(d_freq)
        freq = np.floor(a_freq*d_freq)*tried
        
        while freq.any():
            #calculate the probability for each cell
            prob = freq / np.sum(freq)
            
            #make the choice and set the cell
            random_char = np.random.choice(26, p=prob)
            cell.set_letter(chr(random_char+ord('A')))
            
            #check to ensure the cell's answers are still valid
            a_ans, d_ans = cell.get_answers()
            a_failed = a_ans not in self.clue_repo
            d_failed = d_ans not in self.clue_repo
            if a_failed or d_failed:
                freq[random_char] = 0
            else:
                return (None, True)
        
        #failed - no valid possible letter placements
        cell.set_letter('-')
        
        #return the relevant cell to backtrack to
        return_cell = last_across_cell if last_across_cell != None else last_down_cell
        return (return_cell, False)
    
    """
    Function to randomly pick the clues to go with each answer
    
    returns the fully finished crossword
    """
    def generate_clues(self, d_ans, a_ans):
        # initialize the crossword
        crossword = cw.Crossword(self.size)
        
        #iterate through the answers
        answers = []
        answers.extend(d_ans)
        answers.extend(a_ans)
        for answer in answers:
            if answer == None:
                continue
            word = answer.get_answer()
            if '-' in word:
                return None
            #select the clue and add it to the crossword
            crossword.add_clue(answer, self.clue_repo.select_clue(word))
        return crossword
    
    
    """
    debug function to print the crossword board
    """
    def print_cells(cells):
        for x in cells:
            for y in x:
                if y is None:
                    print('█', end='')
                else:
                    print(y.letter, end='')
            print()       
    
    """
    Function to print the crossword to a file
    """
    def to_txt(crossword, filepath, n):    
        file = open(f'{filepath}\\crossword{n}.txt', "w+")
        file.write(str(crossword))
        file.close()
        
