def split_and_merge(string_, separator):
    swag = []
    for word in string_.split(" "):
        swag.append(separator.join(list(word)))
    return " ".join(swag)