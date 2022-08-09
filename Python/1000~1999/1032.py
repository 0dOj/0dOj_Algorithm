n = int(input())
table = input()
for _ in range(n-1):
    new = input()
    for i in range(len(table)):
        if table[i] != '?' and table[i] != new[i]:
            table = table[:i] + '?' + table[i+1:]

print(table)