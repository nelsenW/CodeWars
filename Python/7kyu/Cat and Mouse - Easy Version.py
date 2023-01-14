def cat_mouse(x):
    return "Caught!" if abs(x.index("C") - x.index("m")) <= 4 else "Escaped!"