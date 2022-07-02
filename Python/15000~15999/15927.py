s = input()
l = len(s)

if s[:l//2] == s[l//2+l%2:][::-1]:
    c0 = s[0]
    for c in s:
        if c0 != c:
            print(l-1)
            exit(0)
    print(-1)
else:
    print(l)