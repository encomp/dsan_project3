### PROBLEM #7

### Design
The solution for the problem was to implement a Trie data structure to be able to provide the handler for a given 
url/path. Such url/path will be search on the Trie that returns its proper Handler. If the provided url/path does not 
have a handler an error handler will be return.

### Space Complexity
In a Trie each node in this structure has to allocate memory for a dictionary of size M, so in terms of space 
complexity, each node also will allocate "N" size in which "N" is the number of keys. As a result, the space complexity 
will be O(MN).

### Running Time Complexity
The running time complexity of add a handler of a paths in a Trie is O(N). In which "N" is the length of the path being
inserted its length is determined based on the number of "/" found. Similarly, to lookup a path on a trie takes O(N) is 
which "N" represents the number "/" found on the path.