import sys

size = 1001
data = [True] * size; data[1] = False

for i in range(2, int(size ** 0.5) + 1):
  if data[i] == True:
    for j in range(i+i, size, i):
      data[j] = False

N = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in range(len(lst)):
    if data[lst[i]] == True:
        cnt += 1

print(cnt)