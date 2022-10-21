
n = int(input())
columns = [False]*(n)
diag1 = [False]*(2*n)
diag2 = [False]*(2*n)
result = [0]
grid = [['.']*n for _ in range(n)]
def search(y, n):
    if y == n:
        result[0] += 1  
        return print(grid)
    for x in range(n):
        if not columns[x] and not diag1[x + y] and not diag2[x - y + n - 1]: 
            grid[y][x] = 'Q'
            columns[x] = diag1[x + y] = diag2[x - y + n - 1] = True 
            search(y + 1, n)
            columns[x] = diag1[x + y] = diag2[x - y + n - 1] = False 
            grid[y][x] = '.'
        
search(0, n)
print(result[0])
'''
[['.', 'Q', '.', '.'], 
['.', '.', '.', 'Q'], 
['Q', '.', '.', '.'], 
['.', '.', 'Q', '.']]


[['.', '.', 'Q', '.'], 
['Q', '.', '.', '.'], 
['.', '.', '.', 'Q'], 
['.', 'Q', '.', '.']]

'''
        
                
    
    
            
            
        
        
        
        
    