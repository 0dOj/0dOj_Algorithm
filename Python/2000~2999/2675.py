import sys

for i in range(int(input())):
    R, S = sys.stdin.readline().split()
    ans = ""

    for j in range(len(S)):
        for k in range(int(R)):
            ans += S[j]

    print(ans)