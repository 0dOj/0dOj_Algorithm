string = input()
target = list(input())

stack = []
for i in string:
    stack.append(i)
    while stack[-len(target):] == target:
        del stack[-len(target):]

if stack: print(''.join(stack))
else: print("FRULA")