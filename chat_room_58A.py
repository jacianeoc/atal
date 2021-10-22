a = input()
ans = 'NO'
l = ['h', 'e', 'l', 'l', 'o']
id = 0
for i in range(0, len(a)):
    if a[i] == l[id]:
        id+=1
        if id == 5:
            ans='YES'
            break

print(ans)