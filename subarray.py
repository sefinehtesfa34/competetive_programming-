l=[1,2,3,4]
lis=[[]]
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        lis.append(l[i:j])
print(lis)