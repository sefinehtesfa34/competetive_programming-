from calendar import c
from collections import defaultdict

def dfs(graph, current, path, answer):
    if len(graph[current]) == 0:
        path.append(current)
        answer.append(path)
        return 
    path.append(current)
    dfs(graph, graph[current][0], path, answer)
    for child in graph[current][1:]:
        dfs(graph, child, [], answer)
        
def main():          
    test = int(input())
    for _ in range(test):
        
        n = int(input())
        paths = list(map(int, input().split())) 
        graph = defaultdict(list)
        root = 1
        for index in range(len(paths)):
            if index + 1 == paths[index]:
                root = index + 1
                continue 
            graph[paths[index]].append(index + 1)
        answer = []
        dfs(graph, root,[root], answer)
        if not answer:
            answer.append([root])
        print(len(answer))
        for each_path in answer:
            print(len(each_path))
            print(*each_path)
        if _ != test - 1:
            print()
        
    
        
        
import sys
import threading
sys.setrecursionlimit(1<<30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
main()
