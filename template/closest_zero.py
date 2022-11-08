from math import *
class Solution:
    def find_closest(self):
        nums = self.get_nums()
        nums.sort()
        left = 0
        right = len(nums) - 1
        negative_closest = -inf
        positive_closest = inf
        
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum < 0:
                if cur_sum > negative_closest:
                    negative_closest = cur_sum 
                left += 1
            if cur_sum > 0 :
                if cur_sum < positive_closest:
                    positive_closest = cur_sum 
                right -=1 
            else:
                return cur_sum 
        
        return min(abs(negative_closest), positive_closest)
    def get_nums(self):
        return list(map(int, input().split()))
solution = Solution()
result = solution.find_closest()            
print(result)
'''

(15 16 19 20 25 1 3 4 5 7 10 14) 

if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
    return mid
if nums[mid] < nums[0]:
    right = mid - 1
else:
    left = mid + 1
return -1



find the index of 5 and return this index
the array is rotated unknown number of times 
which means half of the number to the left
and half of the number to the right are sorted.

N.B  Keep in mind here !

            9
           / \
         6    8 = mid < mid  - 1, move right to mid - 1 
       / |       \
      5  |        7 
    /    |          \
   4     |           2 
         |             \
         |              0
         |            right
left     |             

        if cur_mid < mid + 1
            move left = cur_mid + 1
            
        cur_mid = 9
        if cur_mid > cur_mid - 1 and cur_mid > cur_mid + 1:
            return cur_mid 
'''