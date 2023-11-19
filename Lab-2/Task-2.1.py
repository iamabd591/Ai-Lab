def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])

    return arr


arr = [1, 3, 0, 5, 2, 4, 6, 7, 10]
print("Orignal array:")
print(arr)
selection_sort(arr)
print("Sorted Arr:")
print(arr)
