A = int(input())
B = int(input())

il = A * (B %10)
sip = A * ((B //10) %10)
baek = A * (B//100)

print(il)
print(sip)
print(baek)
print(A*B)

#A = int(input())
#B_str = input()  # B를 숫자가 아닌 문자열 '385'로 받기

# B의 각 자릿수를 인덱스로 접근 (문자이므로 int로 변환 필수!)
#il = A * int(B_str[2])   # '385'의 마지막 글자 '5'
#sip = A * int(B_str[1])  # '385'의 가운데 글자 '8'
#baek = A * int(B_str[0]) # '385'의 첫 글자 '3'

#print(il)
#print(sip)
#print(baek)
#print(A * int(B_str)) # 마지막 전체 곱셈할 땐 B를 숫자로 변환
