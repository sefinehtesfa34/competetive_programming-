matrix=input().split()
domino=[2,1]
val=int(matrix[0])//2
val*=int(matrix[1])
carry=int(matrix[0])%2
carry*=int(matrix[1])
carry=carry//2
val+=carry
print(val)