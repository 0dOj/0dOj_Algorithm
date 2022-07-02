T = int(input())
stack = []

for i in range(T):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))