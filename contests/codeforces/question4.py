from collections import defaultdict


m, n = list(map(int, input().split()))
graph = defaultdict(list)
for index in range(n):
    nums = list(map(int, input().split()))
    graph[index + 1] = nums 

    


'''
R WW R
WWWW
WWRR
RRWW

A B A
WWWW
3 * 2 * 1
  
'''







'''
               1:[2,3,8]   
1: [2]         2:[1,2]
2: [1 2 3]     3:[2,6]
3: [1]         4:[4,7,8]
4: [5 4]       5:[4] 
5: [6 7]       6:[5]
6: [3]         7:[5,7]
7: [7 4]       
8: [1,4]
                1
                | 
                2 
                / \ \ 
                3  6 8
                |   
                8
                | \ \ 
                7  2 4
                |
                5
                     



'''