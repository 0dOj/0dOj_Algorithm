n = int(input())
arr = sorted(list(map(int, input().split())))

if n == 1: print(0); exit(0)

cnt = 0
for k in range(n):
   i = 0
   j = n-1
   while True:
      if   i == k: i += 1
      elif j == k: j -= 1
      if i == j:
         break
      s = arr[i]+arr[j]
      if s == arr[k]:
         cnt += 1
         break
      elif s < arr[k]: i += 1
      else:            j -= 1

print(cnt)