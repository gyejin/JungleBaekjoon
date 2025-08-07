def factorial(n):
    # 1이되면 끝
    if n <= 1:
        return 1
    else:
	# 4->3->2->1
        return n * factorial(n-1)

print(factorial(4))