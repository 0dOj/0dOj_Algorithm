n = int(input())

stack = [int(input()) for _ in range(n)]

cnt = 0
lev1 = stack.pop()
for i in range(n-1):
    lev2 = stack.pop()
    if lev1 <= lev2:
        cnt += lev2-lev1+1
        lev2 = lev1-1
    lev1 = lev2
print(cnt)