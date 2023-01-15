def incrementer(nums):
    for idx, dig in enumerate(nums):
        nums[idx] += idx + 1
        if len(str(nums[idx])) > 1:
            nums[idx] = int(str(nums[idx])[-1])
    return nums