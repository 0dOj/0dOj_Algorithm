from collections import deque

n = int(input())
cnt = n

for _ in range(n):
    s = deque(input())
    st = set()

    while s:
        if s[0] in st:
            cnt -= 1
            break
        if len(s) > 1 and s[0] != s[1]:
            st.add(s[0])
        s.popleft()
    
print(cnt)