T = int(input())
for i in range(T):
  x,y = map(int, input().split())
  dis = y - x
  k = 0
  while not k ** 2 < dis <= (k+1) ** 2:
    k += 1
  average = (k ** 2 + (k+1) ** 2) / 2
  if dis > average:
    print(2*k + 1)
  else:
    print(2*k)