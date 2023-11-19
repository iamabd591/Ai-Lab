def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[i] > arr[j+1]:
                temp = arr[i]
                arr[i] = arr[j+1]
                arr[j+1] = temp
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
    return arr


def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array


def Insertion_sort(array):
    for i in range(len(array)):
        key = array[i+1]
        j = i-1

        while (array[j] >= 0 and key < array[j]):
            array[j+1] = array[j]
            j = j-1
            array[j+1] = key
    return array


name = ['M', 'O', 'H', 'S', 'I', 'N']
Insertion_sort(name)
print("Sorted Array:")
print(name)
