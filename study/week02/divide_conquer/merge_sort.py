def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #divide 나누고
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    #conquer 정렬까지
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

#정렬된 두 리스트를 인수로 받아, 두 리스트를 비교하여 작은 순서대로 result리스트에 삽입, 남은 요소를 추가하여 반환
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result