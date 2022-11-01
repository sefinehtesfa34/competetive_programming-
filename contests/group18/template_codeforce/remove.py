from heapq import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n, m = get_nums()
    graph = []
    output = [["."]*m for _ in range(n)]
    for _ in range(n):
        graph.append(list(input()))
    parent = {(row, col):(row, col) for row in range(n) for col in range(m)}
    size = {(row, col):1 for row in range(n) for col in range(m)}
    
    def find(cell):
        while cell != parent[cell]:
            cell = parent[cell]
        return cell 
    
    def union(cell1, cell2):
        cell1_parent = find(cell1)
        cell2_parent = find(cell2)
        if cell1_parent == cell2_parent:
            return 
        if size[cell1_parent] < size[cell2_parent]:
            cell1_parent, cell2_parent = cell2_parent, cell1_parent 
        size[cell1_parent] += size[cell2_parent]
        parent[cell2_parent] = cell1_parent
        
    for row in range(n):
        for col in range(m):
            if graph[row][col] == "*":
                continue 
            if row > 0 and graph[row - 1][col] == ".":
                union((row, col), (row - 1, col))
            if col > 0 and graph[row][col - 1] == ".":
                union((row, col), (row, col - 1))
            
            
    for row in range(n):
        for col in range(m):
            if graph[row][col] == "*":
                current_parents = set()
                for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row = row + dir[0]
                    new_col = col + dir[1]
                    if new_row < 0 or new_col < 0 or new_row == n or new_col == m:
                        continue
                    if graph[new_row][new_col] == ".":
                        parent_node = find((new_row, new_col))
                        current_parents.add(parent_node)
                
                result = 0
                for par in current_parents:
                    result += size[par]
                output[row][col] = str((1 + result) % 10) if result != 0 else '.'
                 
    for row in output:
        print("".join(row))
                    
            
        
    
main()