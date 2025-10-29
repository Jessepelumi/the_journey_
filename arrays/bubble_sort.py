# implementing a bubble sort 

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def bubbleSortOptimized(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# usage 
arr = [3, 4, 6, 3, 7, 1, 2]
print(f"Sorted: {bubbleSort(arr)}")
print(f"Optimized: {bubbleSortOptimized(arr)}")