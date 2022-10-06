class Solution:
    def count2sBetween0andN(self, n):
        pass 
        '''
        0 1 2 12 20 21 22 23 24 25 26 27 28 29 32 42 52 62 .... 100 102 112 120 ...129 132 1000 1002 1012 1020
            0 10
        100   102 112 120  130 200 202 212 220    
        10
        2 12 20......29 30.....100 ...112    120....129     130.....200...212 220....229 230 
           2  10         70         2             10            70       2*2  10*2    70 * 2
        
        300
        '''
        
solution = Solution()
n = int(input())
result = solution.count2sBetween0andN(n)
print(result)
