n = int(input())
q = [1,2]
for i in range(n-1):
    q.append(sum(q))
    q.pop(0)
print(q[0]%10007)