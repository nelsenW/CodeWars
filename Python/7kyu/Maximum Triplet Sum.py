def max_tri_sum(numbers):
    reversed = numbers.sort(reverse=True)
    max = 0
    count = 0
    for i in range(len(numbers)): 
        if numbers[i] != numbers[i-1]:
            max += numbers[i]
            count += 1
            if count == 3:
                return max