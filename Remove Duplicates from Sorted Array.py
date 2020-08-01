def removeDuplicates(nums) -> int:
    if nums == []:
        return len(nums)

    temp = None
    count = 1
    i = 0

    while 1:
        val = nums[i]
        if val == temp:
            count += 1

        temp = val

        if count > 1:
            nums.remove(val)
            i -= 1
            count -= 1

        i += 1
        if i > len(nums) - 1:
            break

    return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))