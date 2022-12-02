from collections import defaultdict


def dfs(start, visited):
    visited.add(start)
    answer = True 
    for child in graph[start]:
        if child in visited:
            return False 
        answer = answer and dfs(child ,visited)
    return answer 

graph = {'A':['B'], 'B':['C'], 'C':['D'], "D":[]}

'''
A -> B ->C -> D ->A #The is cycle ==> A-> D ->A

'''
is_valid = dfs('A', set())
print(is_valid)
