def encode(message, key):
    alpha = "+abcdefghijklmnopqrstuvwxyz"
    coded = []
    count = 0
    
    for char in message:
        coded.append(alpha.index(char) + int(str(key)[count % len(str(key))]))
        count += 1
    return coded