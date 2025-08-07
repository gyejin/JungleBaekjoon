def binary_search(target, data):
    data.sort()     #데이터 오름차순 정렬
    start = 0
    end = len(data) -1

    while start <= end:
        mid = (start + end) // 2    #중간값

        if data[mid] == target:
            return mid

        elif data[mid] > target:    #중간값이 타겟보다 크면
            end = mid - 1  #end를 중간값+1로 해서 반복
        else:   #중간값이 타겟보다 작으면
            start = mid + 1     #start를 중간값+1로 해서 반복
    return None
    
def recursion_binary_search(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return recursion_binary_search(data, target, start, mid - 1)
    else:
        return recursion_binary_search(data, target, mid + 1, end)
