import pandas as pd
import numpy as np

def ord_(char):
    return ord(char) - ord('A')

class Trie:
    
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.head = TrieNode('-', max_depth)
        
    def __contains__(self, word):
        if(len(word) > self.max_depth):
            return False
        return self.head.find_prefix(0, word)
    
    def insert_word(self, word):
        assert(len(word) <= self.max_depth)
        self.head.insert_word(0, word)
        
    def insert_words(self, words):
        for word in words:
            self.insert_word(word)
        
class TrieNode:
    
    def __init__(self, cur_char, max_depth):
        self.cur_char = cur_char
        self.next_char = [None]*26
        self.depth_counter = [0]*(max_depth+1)
        self.max_depth = max_depth
        self.word_end = False
        
    def find_prefix(self, index, word):
        if(len(word) == index):
            return self.word_end
        if(self.depth_counter[len(word)] == 0):
            return False
        if word[index] == '-':
            #character is a wildcard-- there needs to be at least one character it works for
            for node in self.next_char:
                if node is not None:
                    if(node.find_prefix(index+1, word)):
                        return True
            return False
        else:
            #character is not a wildcard character
            next_node = ord_(word[index])
            if self.next_char[next_node] is None:
                return False
            return self.next_char[next_node].find_prefix(index+1, word)
    
    def insert_word(self, index, word):
        if(len(word) == index):
            self.word_end = True
            return
        self.depth_counter[len(word)] += 1
        next_node = ord_(word[index])
        if self.next_char[next_node] is None:
            self.next_char[next_node] = TrieNode(word[index], self.max_depth)
        self.next_char[next_node].insert_word(index+1, word)


class ClueRepository:
    
    def __init__(self, clue_filepath, max_answer_size):
        self.clue_filepath = clue_filepath
        self.max_answer_size = max_answer_size
        self.clue_dataframe = None
        self.unique_answers = None
        self.answer_trie = None
        self.loaded = False
    
    def is_loaded(self):
        return self.loaded
    
    def load(self):
        if self.loaded:
            return
        self.load_clues()
        self.generate_trie()
        self.loaded = True
    
    def load_clues(self):
        self.clue_dataframe = pd.read_csv(self.clue_filepath)
        self.clean_clues()
        self.unique_answers = self.clue_dataframe.drop_duplicates('answer')['answer'].values

    def clean_clues(self):
        # ignore all na values
        self.clue_dataframe = self.clue_dataframe.dropna()

        # remove all duplicate clues
        self.clue_dataframe = self.clue_dataframe.drop_duplicates('clue')

        # remove all non-alphabetic answers
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.answer.str.isalpha()]

        # remove all answers greater than the max answer size
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.answer.str.len() <= self.max_answer_size]

        # remove all empty answers
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.answer.str.len() > 0]

        # remove all empty clues
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.len() > 0]

        #remove all cross-referential clues
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("across") == False]
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("down") == False]
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("Across") == False]
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("Down") == False]

        #remove all starred clues
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("\*") == False]
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("starred") == False]
        self.clue_dataframe = self.clue_dataframe[self.clue_dataframe.clue.str.contains("Starred") == False]

    def find_frequency(self):
        frequency = [0]*26
        for x in range(0,26):
            char = chr(x + ord('A'))
            frequency[x] = np.sum([str.count(ans, char) for ans in self.unique_answers])
        return frequency
        
    def generate_trie(self):
        self.answer_trie = Trie(self.max_answer_size)
        self.answer_trie.insert_words(self.unique_answers)

    def __contains__(self, prefix):
        return prefix in self.answer_trie
