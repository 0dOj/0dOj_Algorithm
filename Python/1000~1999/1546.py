import sys
N = int(input())

score = list(map(int, sys.stdin.readline().split()))

print(sum(score) / len(score) / max(score) * 100)