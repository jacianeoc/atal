n, a, b,c = [int(x) for x in input().split()]

ans = 0 
for x in range(0, 4001):
  for y in range(0, 4001):
    zlinha = n - (x*a + y*b)
    if zlinha < 0:
      break

    z = (zlinha / c)
    if z == int(z):
      ans = max(ans, z+y+x)

print(int(ans))
