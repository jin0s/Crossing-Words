'''
Initial test of trie.py to see if the Class Trie and TrieNode can be initiated
'''

from src import trie

t = trie.Trie();

def test_init_Trie():
    assert t != None


def test_init_TrieNode():
    tNode = trie.TrieNode('a')
    assert tNode != None
