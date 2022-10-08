'''Long Distance
Medium

Given a list of integers nums, 
return a new list where each element in 
the new list is the number of smaller elements to the right of that 
element in the original input list.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
lst = [3, 4, 9, 6, 1]
Output
[1, 1, 2, 1, 0]
Explanation
There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
Example 2
Input
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Output
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Example 3
Input
lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Output
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]'''

from sortedcontainers import  SortedList
class Solution:
    def solve(self, lst):
        sortedList = SortedList()
        nums = lst[::-1]
        answer = []
        for num in nums:
            index = sortedList.bisect_left(num)
            answer.append(index)
            sortedList.add(num)
        return answer[::-1]
