from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
NtP = {}

for i in range(N):
    NtP[i] = input().rstrip()

PtN = {v:k for k,v in NtP.items()}

for i in range(M):
    inp = input().rstrip()
    if inp.isdigit() == True:
        print(NtP[int(inp) - 1])
    else:
        print(PtN[inp] + 1)