def comb(n, k):
    result = []
    
    def backtrack(current_combination, exNum):
        if len(current_combination) == k:
            result.append(current_combination.copy())
            return

        for i in range(exNum, n+1):
            #선택
            current_combination.append(i)
            #탐색
            backtrack(current_combination, i+1)
            #선택 취소
            current_combination.pop()
            
    backtrack([], 1)
    return result

print(comb(4,2))