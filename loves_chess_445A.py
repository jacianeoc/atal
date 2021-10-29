n,m=map(int,input().split())
ans=[]
for i in range(n):
    arr=input()
    ans.append(list(arr))
o=[]
for i in range(n):
    if i%2==0:
        l=['W','B']*m
    else:
        l=['B','W']*m
    o.append(l[:m])
for i in range(n):
    for j in range(m):
        if ans[i][j]=='-':
            o[i][j]='-'
for i in range(n):
    v=''.join(o[i])
    print(v)