M, N = map(int, input().split())
size = 1000001
data = [True] * size

for i in range(2, size):
  if data[i] == True:
    for j in range(i+i, size, i):
      data[j] = False
    if M <= i <= N:
      print(i)