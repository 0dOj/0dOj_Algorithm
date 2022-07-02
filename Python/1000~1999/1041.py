N = int(input())
A, B, C, D, E, F = map(int, input().split())

a = min(A, F)
b = min(B, E)
c = min(C, D)
dice3 = a+b+c
dice2 = dice3 - max(a, b, c)
dice1 = min(a, b, c)

if N == 1:
  print(A+B+C+D+E+F - max(A,B,C,D,E,F))
else:
  print(((N-2) * (5*N-6) * dice1) + ((8*N-12) * dice2) + (4 * dice3))