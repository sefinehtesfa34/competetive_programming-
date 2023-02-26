from collections import defaultdict
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n  = get_int()
    costs = [0] + get_nums()
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = get_nums()
        graph[a].append(b)
        graph[b].append(a)
    dp = [0]*(n + 1)
    def dfs(root, parent):
        dp[root] = costs[root]
        for child in graph[root]:
            if child == parent:
                continue 
            dfs(child, root)
            dp[root] += dp[child]
            
    dfs(1, None)
    print(dp)
    max_res = max(dp)
    for node in range(2, n + 1):
        
        max_res = max(max_res, 2*(costs[1] - costs[node]) + costs[node])
    print(max_res)
main()
    
    
    
        