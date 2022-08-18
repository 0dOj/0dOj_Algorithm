n = int(input())
st = set()

for _ in range(n):
    st.add(input())

while len(st) == n:
    for i in list(st):
        st.add(i[1:])
        st.remove(i)

print(len(list(st)[0])+1)