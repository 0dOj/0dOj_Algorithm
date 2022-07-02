from sys import stdin
input = stdin.readline

n = int(input())
gw = 0
for _ in range(n):
    s = input().rstrip()

    stack = []
    for i in s:
        if i == 'A':
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append('A')
        elif i == 'B':
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append('B')

    if not stack:
        gw += 1

print(gw)