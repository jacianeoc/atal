n = int(input())

home_uniforms= []
guest_uniforms = []
count = 0
while n > 0:
  numbers = list(map(int, input().split(' ')))
  home_uniforms.append(numbers[0])
  guest_uniforms.append(numbers[1])
  n = n - 1

for home in home_uniforms:
  for j in range(0, len(guest_uniforms)):
    if(home_uniforms.index(home) == j):
      continue
    elif home == guest_uniforms[j]:
      count+=1

print(count)

