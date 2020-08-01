

def permute(nums):

    n = len(nums)
    if n == 0:
        return nums
    elif n == 1:
        return nums
    elif n == 2:
        return (nums, nums[::-1])

    mynums =[]

    for i in range(0, n):
        for j in permute(nums[0:i] + nums[(i+1):n]):
            mynums.append([nums[i]] + j)

    return mynums



a = (permute([1,2,3,4]))

for i in a:
    print(i)