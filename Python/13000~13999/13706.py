N = int(input())
high = N
low = 0

if N == 1:
  i = 1
else:
  while True:
    mid = (high + low) // 2
    if mid ** 2 == N:
      i = mid
      break
    elif mid ** 2 > N:
      high = mid
    elif mid ** 2 < N:
      low = mid

print(i)