'''
Initial test of generator.py to see if the Class CroswordGenerator can be initiated
'''

from src import generator


gen = generator.CrosswordGenerator("Data/clues.csv", "./")


def test_init_CrosswordGenerator():
    assert gen != None

def test_generate():
    gen.generate()
