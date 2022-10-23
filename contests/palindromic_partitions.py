class Solution:
    def get_n(self):
        return int(input())
    
    def get_test(self):
        return int(input())
    
    def palindrome_partitions(self):
        test = self.get_test()
        for _ in range(test):
            n = self.get_n()
            print(self.dp(n, n))
            
    def dp(self, n, sums, index = 1, memo = {}):
        if (index, sums) in memo:
            return memo[(index, sums)]
        if index > n or sums < 0:
            return 0
        
        if sums == 0:
            return 1
        
        take = 0
        if str(index) == str(index)[::-1]:
            take = self.dp(n, sums - index, index, memo)
        not_take = self.dp(n, sums, index + 1,  memo)
        
        memo[(index, sums)] = take + not_take 
        return memo[(index, sums)]
def main():
    solution = Solution()
    solution.palindrome_partitions()
import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start(); thread.join()
    
                
                