n = int(input())
stack = [int(input()) for _ in range(n)]

top = 0
cnt = 0
for i in stack[::-1]:
    if i > top:
        cnt += 1
        top = i

print(cnt)