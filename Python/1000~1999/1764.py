import sys
input = sys.stdin.readline

N, M = map(int, input().split())
didntHeard = [input().rstrip() for _ in range(N)]
didntSee = [input().rstrip() for _ in range(M)]

didntHS = sorted(list(set(didntHeard) & set(didntSee)))

print(len(didntHS))
for i in range(len(didntHS)):
    print(didntHS[i])