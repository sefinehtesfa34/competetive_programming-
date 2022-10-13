from collections import defaultdict, deque
from heapq import heappop, heappush
def treeHeight(root, height = 0):
    if not graph[root]:
        hashmap[height].append(root)
    for child in graph[root]:
        treeHeight(height + 1, child)
t = int(input())
for _ in range(t):
    hashmap = defaultdict(list)
    graph = defaultdict(list)
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for index in range(len(nums)):
        graph[nums[index]].append(index + 2)  
    treeHeight(1)
    heap = []
    for height in hashmap:
        heappush(heap, -1 * (height - 1))
    while k and heap:
        top = -heappop(heap)
        heappush(heap, -top//2)
        k -= 1
    print(max(1, -heappop(heap)))
        
    
        
    '''
    1
    / \ 
    2  3
    / \
    4  5
    '''