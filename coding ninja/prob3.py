'''
Problem statement
You are given two numbers 'a' and 'b' as input.
You must swap the values of 'a' and 'b'.
For Example:
Input: 
'a' = 8, 'b' = 5
Output:
5 8
Explanation:
Initially, the value of 'a' and 'b' is 8 and 5, respectively.
After swapping, the value of 'a' is 5, and the value of 'b' is 8.
'''



#code:
from typing import List

def swapNumber(a: List[int], b: List[int]) -> None:
    # Swapping values using a temporary variable
    temp = a[0]
    a[0] = b[0]
    b[0] = temp
