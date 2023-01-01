class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                comp = -(nums[i]+nums[j])
                c = 0
                if nums[i] == comp:
                    c+=1
                if nums[j] == comp:
                    c+=1
                if count[comp]>c:
                    temp = sorted([comp,nums[i],nums[j]])
                    ans.add(tuple(temp))
                    
        return ans