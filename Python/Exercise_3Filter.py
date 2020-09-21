def filter_list(l):
    """
    l: iterable to be filtered
    return a new list with the strings filtered out
    """
    return list(filter(lambda x: type(x) is int, l))

print(filter_list([1,'a','b',0,15]))
