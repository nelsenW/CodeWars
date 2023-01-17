def two_highest(arg1):
    if not arg1:
        return []
    ans = sorted(set(arg1), reverse=True)
    return [ans[0],ans[1]] if len(ans) > 1 else [ans[0]]