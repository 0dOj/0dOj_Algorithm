A, B, C = map(int, input().split())
def fpow(A, B):
    if B == 1:
        return A
    else:
        x = fpow(A, B//2) % C
        if B % 2 == 0:
            return x*x
        else:
            return x*x*A

ans = fpow(A, B) % C
print(ans)