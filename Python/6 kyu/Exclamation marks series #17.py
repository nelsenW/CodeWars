def balance(left, right):
    lsum = left.count("!") * 2 + left.count("?") * 3
    rsum = right.count("!") * 2 + right.count("?") * 3
    if lsum > rsum:
        return "Left"
    elif rsum > lsum:
        return "Right"
    else:
        return "Balance"
  