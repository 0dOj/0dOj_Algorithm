n = int(input())

edge = {i:set() for i in range(n)}
arr = tuple(map(int, input().split()))

r = int(input())

for i in range(n):
    if arr[i] == -1:
        if i == r:
            print(0)
            exit(0)
        else:
            s = i
    elif arr[i] != r and i != r:
        edge[arr[i]].add(i)

leaf = 0
stack = [s]
while stack:
    x = stack.pop()

    if edge[x]:
        for child in edge[x]:
            stack.append(child)
    else:
        leaf += 1

print(leaf)