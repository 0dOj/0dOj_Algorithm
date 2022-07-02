from sys import stdin
input = stdin.readline
st = [False] * 20

for i in range(int(input())):
    order = input().split()
    
    if order[0] == "add":
        st[int(order[1]) - 1] = True

    elif order[0] == "remove":
        st[int(order[1]) - 1] = False

    elif order[0] == "check":
        if st[int(order[1]) - 1]:
            print(1)
        else:
            print(0)

    elif order[0] == "toggle":
        if st[int(order[1]) - 1]:
            st[int(order[1]) - 1] = False
        else:
            st[int(order[1]) - 1] = True

    elif order[0] == "all":
        for i in range(20):
            st[i] = True
        
    elif order[0] == "empty":
        for i in range(20):
            st[i] = False