class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before
        self.__handler = None
        self.__children = {}

    def get_handler(self):
        return self.__handler

    def set_handler(self, handler):
        self.__handler = handler

    def get_trie(self, path):
        return self.__children[path]

    def has_trie(self, path) -> bool:
        return path in self.__children

    def insert(self, path):
        ## Add a child node in this Trie
        self.__children[path] = RouteTrieNode()
