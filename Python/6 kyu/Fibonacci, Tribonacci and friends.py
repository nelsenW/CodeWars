def Xbonacci(signature,n):
    x = len(signature)
    i = 0
    while len(signature) < n:
        signature.append(sum(signature[i:i+x]))
        i += 1
    return signature[:n]
