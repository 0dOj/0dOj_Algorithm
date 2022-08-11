lst = ['w', 'o', 'l', 'f']
s = input()

while len(lst[0]) < 13:
    s = s.replace(''.join(lst), '1')
    for i in range(4):
        lst[i] += lst[i][0]

for c in s:
    if c != '1':
        print(0)
        exit(0)
print(1)