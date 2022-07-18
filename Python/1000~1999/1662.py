s = input()

f = 1
ans = 0
stack = []
i = 0
while i < len(s):
    if s[i] == '(':
        ans -= f
        if int(s[i-1]) != 0:
            f *= int(s[i-1])
            stack.append(int(s[i-1]))
        else:
            c = 1
            while c != 0:
                i += 1
                if s[i] == '(': c += 1
                elif s[i] == ')': c -= 1
    elif s[i] == ')':
        f //= stack.pop()
    else:
        ans += f
    i += 1
print(ans)