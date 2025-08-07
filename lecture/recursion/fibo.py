def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return tail_fibonacci(n-1, b, a + b)

def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a