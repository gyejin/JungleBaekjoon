def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right =[]

    #divide
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    #conquer
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    return left_sorted + [pivot] + right_sorted