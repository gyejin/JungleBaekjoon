def sum_iter(n, total):
    if n == 0:
        return total
    else:
        return sum_iter(n-1, total + n)

def sum(n):
    return sum_iter(n, 0)