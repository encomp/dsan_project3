### PROBLEM #3

### Design
The solution for the problem #3 was to first sort the entire provided array using heap sort. Upon completion then 
iterate the sorted array from the end to the beginning of the array. The largest element will be part of the first array
the second largest will be part of the second array. The same logic applies until there are no more element left on the 
array. 


### Space Complexity
The sorting algorithm used was Heap sort, however, the implementation provided is an in place sort and it does not use 
recursion as a result the overall space complexity of this solution is O(N). Since, the only additional memory used were
a two variables with the same size as the length of the array.

### Running Time Complexity
The running time complexity of Heap sort is O(N log N). Heapify runs in O(log N). However, you are also building the 
heap and that takes O(n). Thus, the overall time complexity would be O(N log N). After sorting the initial input one 
additional traversal was required to create the array with two elements. The later iteration does not impact the overall 
running time which is O(N log N).