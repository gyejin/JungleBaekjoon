primes = [True for _ in range(10001)]       #10000까지 True 채우기
primes[0] = primes[1] = False       #0, 1 제외

for i in range(2, int(10000**0.5) + 1):     #제곱근 반띵
    if primes[i]:   #i가 True면 검증 시작
        j = 2       #2의 배수부터 시작
        while i * j <= 10000:   #배수 돌아버리기
            primes[i * j] = False   #배수 돌면서 False로 변경
            j += 1  #배수로 쓸 숫자 +1

T = int(input())
for _ in range(T):
    n = int(input())

    a = n // 2  #중앙부터 하는게 차이가 적을 거니까!
    b = n // 2

    while True:
        if primes[a] and primes[b]:
            print(a, b)
            break
        a -= 1
        b += 1  #이러면 자동으로 앞에께 작은 수가 되겠네? 개천재
