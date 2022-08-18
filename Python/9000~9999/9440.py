from collections import deque

while True:
    line = deque(sorted(input().split()[1:]))
    if not line:
        break
    zero = deque()
    while line[0] == '0':
        zero.append(line.popleft())
    
    num1 = ''
    num2 = ''

    while line or zero:
        if len(num1) == len(num2):
            if zero and num1:
                num1 += zero.popleft()
            else:
                num1 += line.popleft()
        else:
            if zero and num2:
                num2 += zero.popleft()
            else:
                num2 += line.popleft()

    print(int(num1)+int(num2))