import sys
nums = list(map(int, sys.stdin.readline().split()))
data = 0

for i in range(len(nums)):
    data += nums[i] ** 2

print(data % 10)