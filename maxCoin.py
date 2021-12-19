piles=[2,4,1,2,7,8]
val=0
for i in range(len(piles)//3):
    mx=max(piles)
    piles.remove(mx)
    mn=min(piles)
    piles.remove(mn)
    mx=max(piles)
    piles.remove(mx)
    val+=mx
print(val)
