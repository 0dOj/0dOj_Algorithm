import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

txt = ""

for i in range(len(A)):
    if A[i] < X:
        txt += str(A[i]) + " "

print(txt)