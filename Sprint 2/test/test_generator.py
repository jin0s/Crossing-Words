'''
Initial test of generator.py to see if the Class CroswordGenerator can be initiated
'''

from src import generator

def test_init_CrosswordGenerator():
    gen = generator.CrosswordGenerator(1, "crossword.txt", "./")
    assert gen != None
