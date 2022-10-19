from collections import defaultdict
def main():
    n, m = list(map(int, input().split()))
    cats = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n - 1):
        parent,child = list(map(int, input().split()))
        graph[parent].append(child)
        graph[child].append(parent)
        
    def dfs(cur, parent, num_cats):
        if cats[cur-1] == 0:
            num_cats = 0
            
        num_cats += cats[cur-1]
        
        if num_cats > m:
            return 0
        
        if parent > 0 and len(graph[cur]) == 1:
            return 1 
        
        counter = 0
        for child in graph[cur]:
            if child == parent:
                continue 
            counter += dfs(child, cur, num_cats)
        return counter 
        
    result = dfs(1,0, 0)
    print(result)
    
import sys
import threading
sys.setrecursionlimit(1<<30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
# main()
