import unittest

from problem5.Trie import Trie


class TrieTest(unittest.TestCase):

    def setUp(self) -> None:
        wordList = [
            "ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"
        ]
        self.my_trie = Trie()
        for word in wordList:
            self.my_trie.insert(word)

    def test_a_suffixes(self):
        trie_node = self.my_trie.find('a')
        suffixes = ['nt', 'nthology', 'ntagonist', 'ntonym']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_an_suffixes(self):
        trie_node = self.my_trie.find('an')
        suffixes = ['t', 'thology', 'tagonist', 'tonym']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_ant_suffixes(self):
        trie_node = self.my_trie.find('ant')
        suffixes = ['hology', 'agonist', 'onym']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_anth_suffixes(self):
        trie_node = self.my_trie.find('anth')
        suffixes = ['ology']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_antho_suffixes(self):
        trie_node = self.my_trie.find('antho')
        suffixes = ['logy']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_antholog_suffixes(self):
        trie_node = self.my_trie.find('antholog')
        suffixes = ['y']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_f_suffixes(self):
        trie_node = self.my_trie.find('f')
        suffixes = ['un', 'unction', 'actory']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_fu_suffixes(self):
        trie_node = self.my_trie.find('fu')
        suffixes = ['n', 'nction']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_fun_suffixes(self):
        trie_node = self.my_trie.find('fun')
        suffixes = ['ction']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_t_suffixes(self):
        trie_node = self.my_trie.find('t')
        suffixes = ['rie', 'rigger', 'rigonometry', 'ripod']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_tr_suffixes(self):
        trie_node = self.my_trie.find('tr')
        suffixes = ['ie', 'igger', 'igonometry', 'ipod']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_tri_suffixes(self):
        trie_node = self.my_trie.find('tri')
        suffixes = ['e', 'gger', 'gonometry', 'pod']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_trig_suffixes(self):
        trie_node = self.my_trie.find('trig')
        suffixes = ['ger', 'onometry']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_trigg_suffixes(self):
        trie_node = self.my_trie.find('trigg')
        suffixes = ['er']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_trigge_suffixes(self):
        trie_node = self.my_trie.find('trigge')
        suffixes = ['r']
        self.assertEqual(suffixes, trie_node.suffixes())

    def test_trigger_suffixes(self):
        trie_node = self.my_trie.find('trigger')
        suffixes = []
        self.assertEqual(suffixes, trie_node.suffixes())


if __name__ == '__main__':
    unittest.main()
