def largest_pair_sum(numbers): 
    numbers.sort(reverse=True)
    return sum(numbers[:2])