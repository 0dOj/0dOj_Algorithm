an, bn = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(an+bn-2*(len(a&b)))