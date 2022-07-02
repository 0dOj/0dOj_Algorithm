import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def LCM(num1, num2):
    if num1 != num2:
        while num1 != 0 and num2 != 0:
            r2 = num1 % num2
            r1 = num2 % num1
            num1 = r1; num2 = r2
    
    return max(num1, num2)

print(LCM(a, b))
print(a * b // LCM(a, b))