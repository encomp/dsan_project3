from algorithms.RouteTrie import RouteTrie


class Router:
    def __init__(self, root_handler, handler):
        self.__router = RouteTrie()
        self.__default_handler = handler
        self.add_handler('/', root_handler)

    def add_handler(self, path, handler):
        paths = self.split_path(path)
        if paths:
            self.__router.insert(paths, handler)
            return True
        return False

    def lookup(self, path):
        paths = self.split_path(path)
        if paths:
            current = self.__router.find(paths)
            if current and current.get_handler():
                return current.get_handler()
        return self.__default_handler

    def split_path(self, path):
        if path and len(path.strip()) > 0:
            return path.strip().replace('/', ' ').rstrip().split(' ')
        return None
