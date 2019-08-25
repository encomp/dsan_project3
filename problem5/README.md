### PROBLEM #5

### Design
The solution for the problem was to implement a Trie data structure to be able to provide the suffixes for a given 
prefix typed by the user. Such prefix will be search on the Trie that returns the given TrieNode. This node is used to 
recursively retrieve all the suffixes that it might have and provide them as an array. 

### Space Complexity
In a Trie each node in this structure has to allocate memory for a dictionary of size M, so in terms of space 
complexity, each node also will allocate "N" size in which "N" is the number of keys. As a result, the space complexity 
will be O(MN).

### Running Time Complexity
The running time complexity of inserting a set of words in a Trie is O(MN). In which "M" is the length of the word being
inserted and "N" the total number of words. Similarly, finding a prefix on a trie takes O(N) is which "N" represents the 
number of characters of the prefix. Lastly, find the suffixes for a Node will take O(MN) in which "M" represent all the 
keys that the node has and "N" the remaining length of each word.
 