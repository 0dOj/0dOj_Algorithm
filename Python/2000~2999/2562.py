nums = []

for i in range(0, 9):
    nums.append(int(input()))
    
mx = max(nums)
print(mx)
print(nums.index(mx) + 1)