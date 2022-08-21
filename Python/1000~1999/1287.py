s = input()

ops = ('(', '+', '-', '*', '/', ')')

if '()' in s:
    print('ROCK')
    exit(0)

for i in ops[1:5]:
    for j in range(len(s)):
        if i == s[j] and (j == 0 or j == len(s)-1 or s[j-1] in ops[:5] or s[j+1] in ops[1:]):
            print('ROCK')
            exit(0)

s = s.replace('/', '//')

try:
    print(eval(s))
except:
    print('ROCK')