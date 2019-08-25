### PROBLEM #6

### Design
The solution for the problem was to define two variable one for max one for min. These variables are initialized with 
the first value of the given array. Then the array is traverse only one from the second element until the last element 
of the array. Each iteration it compares the max with the current element of the array and if the max element is less 
than the current element then the max element will be the current element in the array. The similar approach was used to
calculate the min element of the array. 

### Space Complexity
The space complexity of the solution is O(1). Since there are only two variables being used to provide the proper max 
and min elements.

### Running Time Complexity
The running time complexity is O(N). A single traversal of the array is performed to determine the max and min elements 
of the array.