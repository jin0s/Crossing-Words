from src import trie

t = trie.Trie();

# add 'hello' to the Trie

# This should return True
def test_find_prefix():
    result = t.find_prefix(1, 'hello');
    assert result == True;
