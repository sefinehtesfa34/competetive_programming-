class Solution:
    def longestInterval(self,intervals):
        '''
        [1,2], [4,5],[6,12], [3,30]
        _____
               ____________
                             ______________
              _________________________________________               
        
        '''
        intervals.sort(key= lambda x:x[1])
        start = intervals[0][1]
        counter = 1
        for interval in intervals:
            if start < interval[0]:
                counter += 1
                start = interval[1]
        return counter 
intervals = []
N = int(input())
for _ in range(N):
    interval = list(map(int,input().split()))
    intervals.append(interval) 
solution = Solution()
longestInterval = solution.longestInterval(intervals)
print(longestInterval)
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
        
        
    
        
        
     
    
    