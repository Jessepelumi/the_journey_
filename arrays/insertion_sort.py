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
    n = len(arr)

    for i in range(1, n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        
        arr[insert_index] = current_value

    return arr

# Usage
arr = [10, 3, 4, 6, 2, 7, 5, 1]
print(f"Sorted: {insertionSort(arr.copy())}")
print(f"Swap sorted: {insertionSortSwap(arr.copy())}")
print(f"Optimized: {insertionSortOptemized(arr.copy())}")
