from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(N):
    txt = input().rstrip().split()
    dic[txt[0]] = txt[1]

for i in range(M):
    txt = input().rstrip()
    print(dic[txt])