import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    PS = input().rstrip()
    lft = 0; rgt = 0

    for i in range(0, len(PS)):
        if PS[i] == "(":
            lft += 1
        elif PS[i] == ")":
            rgt += 1
        
        if lft < rgt:
            break

    if lft == rgt:
        print("YES")
    else:
        print("NO")