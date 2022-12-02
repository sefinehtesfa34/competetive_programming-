from ast import List
from cmath import inf


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bags = {per:0 for per in range(k)}
        self.min_unfairness = inf
        chosen = {index:False for index in range(len(cookies))}
        def find_min(bags, remaining):
            cur_max = remaining
            for bag in bags:
                cur_max = max(cur_max, bags[bag])
            self.min_unfairness = min(self.min_unfairness, cur_max)
            
        def recursive(chosen, index, bags):
            remaining = 0
            for index in chosen:
                if chosen[index] == False:
                    remaining += cookies[index]
            find_min(bags, remaining)
            
            if index == len(cookies):
                find_min(bags, 0)
                return
            
            for bag in range(k - 1):
                bags[bag] += cookies[index]
                chosen[index] = True
                recursive(chosen, index + 1, bags)
                bags[bag] -= cookies[index]
                chosen[index] = False
        recursive(chosen, 0, bags)
        
        return self.min_unfairness
    
    
solution = Solution()
cookies = list(map(int, input().split()))
result = solution.distributeCookies(cookies)
print(result)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                