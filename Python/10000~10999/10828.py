import sys

N = int(sys.stdin.readline())
stk = []

for i in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == "push":
        stk.append(order[1])
        
    elif order[0] == "pop":
        if len(stk) != 0:
            print(stk.pop())
        else:
            print("-1")
            
    elif order[0] == "size":
        print(len(stk))
        
    elif order[0] == "empty":
        if len(stk) == 0:
            print("1")
        else:
            print("0")
            
    elif order[0] == "top":
        if len(stk) != 0:
            print(stk[-1])
        else:
            print("-1")