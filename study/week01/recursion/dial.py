def dial(digits):
    # 예외 처리: 입력이 비어있으면 빈 리스트 반환
    if not digits:
        return []

    result = []
    # 1. 딕셔너리 키를 문자열로 수정
    phone_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def backtrack(index, current_string):
        # 5. 베이스 케이스: 완성된 문자열을 결과에 추가
        if len(current_string) == len(digits):
            result.append(current_string)
            return

        # 3. 현재 index에 해당하는 숫자 가져오기
        current_digit = digits[index]
        # 그 숫자에 해당하는 문자들 (e.g., "abc")
        letters_to_try = phone_map[current_digit]

        # 3. 현재 숫자의 문자들을 순회하는 for문 하나만 사용
        for letter in letters_to_try:
            # 4. 문자를 선택하고 바로 재귀 호출!
            # (문자열은 불변이라 + 연산으로 새 문자열을 넘겨주면 pop()이 필요없어 편함)
            backtrack(index + 1, current_string + letter)

    # 2. 빈 문자열 "" 로 시작!
    backtrack(0, "")
    return result

print(dial("23"))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

"""
def dial(digits):
    result = []
    dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    def backtrack(index, current_string):
        if len(digits) == index:
            result.append(current_string[index])
            return
        
        for i in range(len(digits)):
            for j in range(len(dict[digits[i]])):
                current_string.append(dict[digits[i]][j])

            backtrack(index+1, current_string)

    backtrack(0, [])
    return result

print(dial("23"))
"""