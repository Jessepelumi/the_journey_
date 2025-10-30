# Insertion sort implementation

def insertionSort(arr:list):
    n = len(arr)

    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                sort = arr.pop(i)
                arr.insert(j, sort)

    return arr

def insertionSortSwap(arr:list):
    n = len(arr)

    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

def insertionSortOptemized(arr:list):
    pass

# Usage
arr = [10, 3, 4, 6, 2, 7, 5, 1]
print(f"Sorted: {insertionSort(arr.copy())}")
print(f"Swap sorted: {insertionSortSwap(arr.copy())}")

# arr[j], arr[i] = arr[i], arr[j]