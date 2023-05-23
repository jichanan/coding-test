ans = []
nums = [1,2,3,4,0]
index = [0,1,2,3,0]

for i in range(len(nums)):
    ans.insert(index[i], nums[i])

print(ans)

    