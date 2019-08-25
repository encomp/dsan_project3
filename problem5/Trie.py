class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.__is_word = False
        self.__children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.__children[char] = TrieNode()

    def is_word(self):
        return self.__is_word

    def set_is_word(self, is_word):
        self.__is_word = is_word

    def get_trie(self, char):
        return self.__children[char]

    def has(self, char) -> bool:
        return char in self.__children

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = list()
        self.__suffixes(suffix, suffixes, '')
        return suffixes

    def __suffixes(self, suffix, suffixes, word):
        for key in self.__children:
            trie = self.get_trie(key)
            if trie.is_word():
                suffixes.append(word + key)
            trie.__suffixes(suffix, suffixes, word + key)


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.__root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.__root
        for char in word:
            if not current.has(char):
                current.insert(char)
            current = current.get_trie(char)
        current.set_is_word(True)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.__root
        for char in prefix:
            if current_node.has(char):
                current_node = current_node.get_trie(char)
            else:
                return None
        return current_node
