from algorithms.RouteTrieNode import RouteTrieNode

class RouteTrie:
    def __init__(self):
        self.__root = RouteTrieNode()

    def insert(self, paths, handler):
        current = self.__root
        for char in paths:
            if not current.has_trie(char):
                current.insert(char)
            current = current.get_trie(char)
        current.set_handler(handler)

    def find(self, paths):
        current_node = self.__root
        for path in paths:
            if current_node.has_trie(path):
                current_node = current_node.get_trie(path)
            else:
                return None
        return current_node