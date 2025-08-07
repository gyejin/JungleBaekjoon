#유클리드 호제법 GCD(a, b) = GCD(b, a % b)
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

result = GCD(48, 18)
print(result)
