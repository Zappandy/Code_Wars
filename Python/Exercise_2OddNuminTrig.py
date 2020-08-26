def row_sum_odd_numbers(n):
    """
    n: num of odd elements to be added. This number defines
    the starting odd number which in the function is defined as start
    return: sum of numbers
    """
    start = n**2 - (n - 1)
    row = []
    for i in range(n):
        row.append(start)
        start += 2
    return sum(row)
