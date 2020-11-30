first = int(input())
second = int(input())
if first > second:
  for i in range(second, first):
    print(i)
else:
  for i in range(first, second):
    print(i)
