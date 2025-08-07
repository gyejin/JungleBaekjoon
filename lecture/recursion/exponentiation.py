def exponentiation(base, exponent):
    if exponent == 0:
        return 1
    else:
        # 거듭제곱 계산: base^exponent = base * base^(exponent - 1)
        return base * exponentiation(base, exponent - 1)
    
def tail_exponentiation(base, exponent, result):
    if exponent == 0:
        return result
    else:
        # 꼬리 재귀를 사용하여 거듭제곱 계산
        return tail_exponentiation(base, exponent - 1, result * base)

def exponentiation_iter(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def fast_exponentiation(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        # 짝수의 경우 //2 몫을 사용하여 거듭제곱 계산
        return fast_exponentiation(base * base, exponent // 2)
    else:
        # 홀수의 경우 -1을 사용하여 거듭제곱 계산
        return base * fast_exponentiation(base, exponent - 1)