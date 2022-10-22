'''

310. Minimum Height Trees
A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges 
where edges[i] = [ai, bi] indicates that there is an undirected edge between 
the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. 
Among all possible rooted trees, those with minimum height (i.e. min(h))  
are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between 
the root and a leaf.


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

'''

from math import inf
m, s = list(map(int, input().split()))
min_num = ''
max_num = ''
digit = 0
while s > 0:
    index = 9 
    while index > s:
        index -=1
     
    max_num += str(index)
    s -= index
if len(max_num) > m:
    print(-1, -1)
else:
    min_num = max_num[::-1]
    max_num += str('0'*(m -len(max_num))) 
    min_num += str('0'*(m - len(min_num)))

     

# import threading
# threading.stack_size(1 << 27)
# thread = threading.Thread(target=main)
# thread.start(); 
# thread.join()
# main()
def main(s, m):
    num1 = ''
    num2 = ''
    for index in range(m):
        cur = min(s, 9)
        num1 += cur + '0'
        s -= cur
    if s >0:
        return print(-1, -1)
    num2 = num1[::-1]
    index = 0
    while index < len(num2) and num2[index] == '0':
        index += 1
    if index < len(num2):
        num2 = list(num2)
        num2[0] = str(1) 
        num2[index] = str(int(num2[index] - 1))
    return print(num2, num1)
main()
'''

row = 0 :9 2 8 4 5 3
row = 1 :7 8 1 4 6 0
prev = [0, 0]
prev[0] = max(prev[0], current_num + prev[1])
prev[1] = max(prev[1], current_num + prev[0])
[8 + 9, 7 + 2]


[17, 9] 



'''
n  = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

def dp(i, j, turn):
    # base case
    if i == len(team1) and turn == 1:
        return 0
    if j == len(team2) and turn == 2:
        return 0
    
    if turn == 1:
        chose = team1[i] + dp(i + 1, i + 1, 2)
        not_chose = dp(i + 1, j, turn)
        return max(chose, not_chose)
    chose = team2[j] + dp(j + 1, j + 1, 1)
    not_chose = dp(i, j + 1, turn)
    return max(chose, not_chose)
result = max(dp(0, 0, 1), dp(0, 0, 2))
print(result)




























































































































    
    
    

