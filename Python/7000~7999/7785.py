from sys import stdin
input = stdin.readline

giigle = set([])

for i in range(int(input())):
    inp = input().rstrip().split()
    if inp[1] == "enter":
        giigle.add(inp[0])
    elif inp[1] == "leave":
        giigle.remove(inp[0])

giigle = sorted(list(giigle), reverse=True)
for i in giigle: print(i)