def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return 0
    else:
        return num * factorial(num-1)

N = int(input())
print(factorial(N))
