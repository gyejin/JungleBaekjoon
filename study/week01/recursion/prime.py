def slow_is_prime_number(n):
    for i in range(2,n): # 2부터 n-1까지
        if n % i == 0: # 하나라도 나누어 떨어지는 수가 있다면
            return False # 소수가 아니다.
	
    return True

# 개선된 소수 판별 함수
def fast_is_prime_number(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    
    return True

def prime_numbers(n):
    arr = [i for i in range(n+1)] # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i*i, n+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

def is_prime_num(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

def prime_num(n):
    arr = [i for i in range(n+1)]
    end = int(n ** (1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] == 0
    return [i for i in arr[2:] if arr[i]]
