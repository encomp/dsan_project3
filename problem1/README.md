### PROBLEM #1

### Design
The square root solution borrow the binary search approach to determine the floor square root for a given number. In 
this approach the square root of a number is found if following condition is met:
 
  * if the midElement == number / mid
  
If the condition above is met it implies that square of the number has been found. If this is not the case the it 
continues searching to the left or to its right. The search is being performed recursively.

### Space Complexity
The function make use of recursion which creates a stack that is populated every time the function is called. In the 
stack the user and group are being stored. As a result, the space complexity of the recursive algorithm is proportional 
to maximum depth of recursion tree generated. Therefore, if each function call of the recursive algorithm takes O(M) 
space and if the maximum depth of recursion tree is "N" then the space complexity of recursive algorithm would be O(NM).

### Running Time Complexity
The running time complexity O(log N). Since in the reduce the length of "N" by half on every recursive call.