f = 0
c = 0
s = input(); l = len(s)

i = 0
while i < l:
    if i != l-1 and s[i:i+2] == '()':
        c += f
        i += 1
    elif s[i] == '(':
        c += 1
        f += 1
    elif s[i] == ')':
        f -= 1
    i += 1
print(c)