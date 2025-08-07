num1, num2 = input().split()
num3 = int(num1[::-1])
num4 = int(num2[::-1])
print(max(num3, num4))
