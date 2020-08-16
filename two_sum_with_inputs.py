nums = [2, 7, 11, 15]

num = 0
for x in range(0, len(nums)-1):
    for y in range(x+1, len(nums)):
        if nums[x] + nums[y] == 9:
            print("value:", nums[x], nums[y])
            print("indices: ", x, y)
            num = 1
        break
if num == 0:
    print("Target not achieved")