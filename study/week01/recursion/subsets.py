def subset(num):
    result = []
    #종료 조건 : index가 숫자 끝까지 가면 더이상 처리할 수가 없으니 end
    def backtrack(index, current_subset):
        if len(num) == index:
            result.append(current_subset.copy())
            return

        backtrack(index+1, current_subset)

        current_subset.append(num[index])

        backtrack(index+1, current_subset)

        current_subset.pop()
    
    backtrack(0, [])
    return result

print(subset([1,2,3]))
    #선택 : 
    #탐색 :
    #선택 취소 :

    #입력이 [1,2,3,4]
    # [1] -> [1, 2] -> [1,2,3] -> [1,2,3,4] -> [1,2,3] -> [1,2] -> [1,2,4]