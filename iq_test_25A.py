n = int(input())
numbers = list(map(int, input().split(' ')))
list_num = []

for number in numbers:
  list_num.append(number % 2 )

if len(numbers) == n:
  if list_num.count(1) == 1: 
    print(list_num.index(1) +1)
  elif list_num.count(0) == 1: 
    print(list_num.index(0) +1)
