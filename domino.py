mat=input().strip().split()    
val=int(mat[0])//2
carry=int(mat[0])%2
val*=int(mat[1])
carry*=int(mat[1])
carry=carry//2
val+=carry
print(val)