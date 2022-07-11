s = input()
mid = len(s) // 2

if s[:mid] == s[len(s):len(s)-mid-1:-1]:
    print(1)
else:
    print(0)