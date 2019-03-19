"""
Unit tests for Trie, TrieNode, and ClueRepository
"""

#TRIE UNIT TESTs
def test_init_trie():
    md = 5
    trie = Trie(md)
    assert(trie is not None)

def test_insert_word_trie():
    md = 5
    trie = Trie(md)
    trie.insert_word("A")
    assert(trie.head.next_char[0] is not None)

def test_contains_trie():
    md = 5
    trie = Trie(md)
    trie.insert_word("AAA")
    assert("AAA" in trie)
    assert("AAB" not in trie)

def test_insert_words_trie():
    md = 5
    trie = Trie(md)
    trie.insert_words(["AAA","AAB"])
    assert("AAA" in trie)
    assert("AAB" in trie)

#TRIENODE UNIT TESTS - LARGELY REDUNDANT   
def test_init_trienode():
    md = 5
    char = 'C'
    trienode = TrieNode(char, md)
    assert(trienode is not None)

def test_insert_word_trienode():
    md = 5
    char = 'C'
    trienode = TrieNode(char, md)
    trienode.insert_word(0,"A")
    assert(trienode.next_char[0] is not None)

def test_find_prefix_trienode():
    md = 5
    char = 'C'
    trienode = TrieNode(char, md)
    trienode.insert_word(0,"AA")
    assert(trienode.find_prefix(0,"AA"))
    
#CLUE REPOSITORY UNIT TESTS
"""
The Functions find_frequency(), generate_trie(), clean_clues(), and load_clues() are all only called once
and are split apart only to improve the readability and compartmentality of the code.
They are tested implicitly by the unit function for load()
"""
def create_temp_df():
    df = pd.DataFrame({"answer":["AAA","AaA","123","","FFF","AAFS"], "clue":["A","B","C","D","E","F"]})
    df.to_csv("temp.csv")

def test_init_cr():
    create_temp_df()
    cr = ClueRepository("temp.csv", 15)
    assert(cr is not None)
    
def test_is_loaded_cr():
    create_temp_df()
    cr = ClueRepository("temp.csv", 15)
    assert(not cr.is_loaded())
    cr.load()
    assert(cr.is_loaded())
    
def test_select_clue_cr():
    create_temp_df()
    cr = ClueRepository("temp.csv", 15)
    cr.load()
    assert(cr.select_clue("AAA") == "A")

def test_get_frequency_cr():
    create_temp_df()
    cr = ClueRepository("temp.csv", 15)
    cr.load()
    assert(cr.get_frequency(0)[0] == 2)
    
def test_load_cr():
    create_temp_df()
    cr = ClueRepository("temp.csv", 15)
    cr.load()
    assert("AAA" in cr and "AAFS" in cr and "123" not in cr)
