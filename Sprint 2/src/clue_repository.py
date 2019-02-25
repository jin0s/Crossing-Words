import pandas as pd
import numpy as np

def ord_(char):
    return ord(char) - ord('A')

class Trie:
    
    def __init__(self, _max_depth):
        self.max_depth = _max_depth
        self.head = TrieNode('-', _max_depth)
        self.depth_counter = [0]*(_max_depth+1)
        
    def find_prefix(self, word):
        if(len(word) > self.max_depth):
            return False
        return self.head.find_prefix(0, word)
    
    def insert_word(self, word):
        assert(len(word) <= self.max_depth)
        self.depth_counter[len(word)] += 1
        self.head.insert_word(0, word)
        
    def insert_words(self, words):
        for word in words:
            self.insert_word(word)
        
class TrieNode:
    
    def __init__(self, _cur_char, _max_depth):
        self.cur_char = _cur_char
        self.next_char = [None]*26
        self.max_depth = _max_depth
        self.depth_counter = [0] *(_max_depth+1)
        
    def find_prefix(self, index, word):
        if(len(word) == index):
            return True
        next_node = ord_(word[index])
        if self.next_char[next_node] is None:
            return False
        return self.next_char[next_node].find_prefix(index+1, word)
    
    def insert_word(self, index, word):
        if(len(word) == index):
            return
        self.depth_counter[len(word)-index] += 1
        next_node = ord_(word[index])
        if self.next_char[next_node] is None:
            self.next_char[next_node] = TrieNode(word[index], self.max_depth)
        self.next_char[next_node].insert_word(index+1, word)


class ClueRepository:
    
    def __init__(self, _clue_filepath, _max_answer_size):
        self.clue_filepath = _clue_filepath
        self.max_answer_size = _max_answer_size
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
    
    def generate_trie(self):
        self.answer_trie = Trie(self.max_answer_size)
        self.answer_trie.insert_words(self.unique_answers)
    
    def __contains__(self, prefix):
        return self.answer_trie.find_prefix(prefix)
    
