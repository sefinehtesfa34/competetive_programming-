from cmath import inf
class Solution:
    def minSwitchs(self,nums):
        # hashmap =  {1:1,0:0}
        # minswitch = 0
        # for num in nums:
        #     on = hashmap[num]
        #     if on == 0:
        #         minswitch += 1
        #         hashmap[1] = 0
        #         hashmap[0] = 1
        # return minswitch
        cost = 0
        for num in nums:
            if cost % 2 != 0:
                num =  not num
            if num == 0:
                cost += 1
        return cost    
                

        # '''
        
        # [0 0 1 0 0 1]
        # 1 2  3 
        # '''

nums = list(map(int, input().split()))
solution = Solution()
minswitchs = solution.minSwitchs(nums)
print(minswitchs)
