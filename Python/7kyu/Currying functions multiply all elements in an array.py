def multiply_all(arr):
    def curry(int):
        return list(map(lambda x: x * int, arr))
    return curry
        