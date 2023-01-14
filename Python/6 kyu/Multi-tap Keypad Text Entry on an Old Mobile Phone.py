def presses(phrase):
    alpha4 = "+abc2def3ghi4jkl5mno6tuv8"
    alpha5 = "+pqrs7wxyz9"
    alpha1 = "1 *#"
    count = 0
    for char in phrase.lower():
        if char in alpha4:
            if abs(alpha4.index(char) % 4) != 0:
                count += abs(alpha4.index(char) % 4)  
            else:
                count += 4
        elif char in alpha5:
            if abs(alpha5.index(char) % 5) != 0:
                count += abs(alpha5.index(char) % 5)  
            else:
                count += 5
        elif char in alpha1:
            count +=  1
        else:
            count += 2
        print(char, count)
    return count