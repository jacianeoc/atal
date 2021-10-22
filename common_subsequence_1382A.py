n = int(input())
for i in range(0, n):
  m = list(map(int, input().split()))
  a = set(map(int, input().split()))
  b = set(map(int, input().split()))
  merge = a & b
  if merge :
    print('YES')
    print(1, merge.pop())
  else:
    print('NO')
