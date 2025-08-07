def perm(num):
    result = []
    vst = [False] * len(num)
    def backtracking(current_permutation):
        if len(current_permutation) == len(num):
            result.append(current_permutation.copy())
            return

        for i in range(len(num)):
            if not vst[i]:
                current_permutation.append(num[i])
                vst[i] = True

                backtracking(current_permutation)

                current_permutation.pop()
                vst[i] = False
    backtracking([])
    return result 

print(perm([1,2,3]))


"""
def permutation(nums):
    numList = []
    vst = [False] * len(nums)
    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            numList.append(current_permutation.copy())
            return

        #0, 1, 2 도러
        for i in range(len(nums)):
            if not vst[i]:
                #선택
                current_permutation.append(nums[i])
                vst[i] = True
                #탐색
                backtrack(current_permutation)
                #선택취소
                current_permutation.pop()
                vst[i] = False
    backtrack([])
    return numList
                
print(permutation([1,2,3]))
"""
