### PROBLEM #4

### Design
The solution for the problem was to implement to perform a single traversal of the array using a left pointer. The array 
also is being traverse both ways using a right pointer from the end to the beginning and/or current to end based on the 
direction flag called increment. There is also another flag that determine which element is currently being sorted 
called c_l. The left flag only advances if the c_l the current position is equal to c_l, however, the right pointer is 
always advance at the end of the loop. if the left element is bigger to the right element then this element are swapped.
Lastly if the the left and right crosses the direction of the right pointer is changed. 

### Space Complexity
The space complexity of the solution is O(1), since the array is being sorted in place and there is no auxiliary space 
being used. But it uses O(N) if we consider the input list provided to the function.

### Running Time Complexity
The running time complexity is O(N). Since, there is only a single traversal of the array with length "N".