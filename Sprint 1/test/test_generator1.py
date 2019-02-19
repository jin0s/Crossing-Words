'''
Unit test for generate function in generator.py
'''

from src import generator

def test_generate():
    gen = generator.CrosswordGenerator(1, "clues.csv", "./")
    gen.generate()
    try:
        ex_filename = "empty_crossword.txt"
        ex_file = open(ex_filename, "r")
        ex_string = ex_file.read()
        ex_file.close()
        try:
            gen_filename = "crossword0.txt"
            gen_file = open(gen_filename, "r")
            gen_string =  gen_file.read()
            gen_file.close()
            assert gen_string == ex_string
        except FileNotFoundError:
            print("File not generated")
            raise
        except AssertionError:
            print("File incorrect")
            raise
    except FileNotFoundError:
        print("Example file missing")
        raise
