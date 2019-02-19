from src import generator

gen = generator.CrosswordGenerator(1, "../clues.csv", "./")

def test_generate():
    gen.generate()
