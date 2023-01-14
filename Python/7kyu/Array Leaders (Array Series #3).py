def array_leaders(numbers):
    ans = []
    for idx, num in enumerate(numbers):
        if num > sum(numbers[idx + 1:]):
            ans.append(num)
            
    return ans