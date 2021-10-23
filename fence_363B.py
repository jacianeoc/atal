n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]

ans = 1
ini = sum(h[0:k])
s = ini
for i in range(k, n):
  s -= h[i-k]
  s +=h[i]
  if s < ini:
    s = ini
    ans = i-k+2

  
print(ans)

