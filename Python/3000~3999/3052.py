lst = []
for i in range(0, 10):
    n = int(input())
    lst.append(n % 42)

lst = set(lst)
print(len(lst))