from collections import defaultdict, deque
def get_n_m():
    return list(map(int, input().split()))
def is_cat():
    return list(map(int, input().split()))
def edges():
    return list(map(int, input().split()))
def dfs(graph, cats, n, m, keep, start, parent):
    if cats[start - 1] == 1:
        m -= 1
    else:
        m = keep 
    if m == -1:
        return 0
    if not graph[start]:
        return 1 
    counter = 0
    for child in graph[start]:
        if child == parent:
            continue 
        counter += dfs(graph, cats, n, m, keep, child, start)
    return counter 

def main():
    n, m = get_n_m()
    cats = is_cat()
    graph = defaultdict(list)
    for _ in range(n - 1):
        parent, child =  edges()
        graph[parent].append(child)
        graph[child].append(parent)
    result = dfs(graph, cats, n, m, m, 1, 0)
    print(result)
main()

    