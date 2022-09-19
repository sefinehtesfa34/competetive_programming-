'''
There was a row of empty(.) and filled cells(X).
Find the minimum number of moves required to make 
people seat together.
constraint 1 <= N <= 1e6
    X..X...X
    0  2   8  14  22  37
    prev = prev + iter * cur
    iter ++;
'''
class Solution:
    def minMoves(self,seats):        
        prev = 0
        iter = 0
        cur = 0
        hashmap = {}
        for index,cell in enumerate(seats):
            if cell == "X":
                prev += iter * cur 
                hashmap[index] = prev
                cur = 0
                iter += 1 
            else:
                cur += 1
        prev = 0
        iter = 0
        cur = 0
        for index in range(len(seats)-1,-1,-1):
            if seats[index] == "X":
                prev += iter * cur 
                hashmap[index] += prev
                cur = 0
                iter += 1
            else:
                cur += 1
        return min(hashmap.values())
    
solution = Solution()
seats  = input()
result = solution.minMoves(seats)
print(result)
