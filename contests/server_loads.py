class Solution:
    def server_loads(self):
        loads = self.get_loads()
        total_sum = sum(loads)
        self.answer = total_sum
        
        def dp(index, cur_sum):    
            if index == len(loads):
                return total_sum
            
            self.answer = min(self.answer, abs(total_sum - cur_sum))
            dp(index + 1, cur_sum + loads[index])
            dp(index + 1, cur_sum)
            
        dp(0, 0)
        return print(self.answer) 
    
    def get_loads(self):
        return list(map(int, input().split()))
solution = Solution()
solution.server_loads()

    