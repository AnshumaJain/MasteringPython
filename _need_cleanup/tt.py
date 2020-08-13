def removeElement(nums, val: int) -> int:
    if nums == []:
        return len(nums)

    temp = None
    count = 1
    i = 0

    while 1:
        element = nums[i]
        if element == val:
            nums.remove(element)
            i -= 1

        i += 1
        if i > len(nums) - 1:
            break

    print(nums)
    return len(nums)

print(removeElement([0,1,2,2,3,0,4,2], 2))