# Insertion sort implementation

def insertionSort(arr:list):
    n = len(arr)

    for i in range(1, n):
        
        for j in range(i):
            if arr[j] > arr[i]:
                val = arr.pop(i)
                arr.insert(j, val)

    return arr

# Usage
arr = [10, 3, 4, 6, 2, 7, 5, 1]
print(insertionSort(arr))