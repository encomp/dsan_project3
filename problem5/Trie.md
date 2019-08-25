
# Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Give it a try by implementing the `TrieNode` and `Trie` classes below!


```python
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
```

# Finding Suffixes

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)


```python
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
```

# Testing it all out

Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.


```python
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
```


```python
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
```


<p>Failed to display Jupyter Widget of type <code>interactive</code>.</p>
<p>
  If you're reading this message in the Jupyter Notebook or JupyterLab Notebook, it may mean
  that the widgets JavaScript is still loading. If this message persists, it
  likely means that the widgets JavaScript library is either not installed or
  not enabled. See the <a href="https://ipywidgets.readthedocs.io/en/stable/user_install.html">Jupyter
  Widgets Documentation</a> for setup instructions.
</p>
<p>
  If you're reading this message in another frontend (for example, a static
  rendering on GitHub or <a href="https://nbviewer.jupyter.org/">NBViewer</a>),
  it may mean that your frontend doesn't currently support widgets.
</p>




```python

```
