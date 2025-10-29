# Bubble sort implementation

"""
Sorting algorithm where large element "bubble" up to the end of the array.
Each element of the array is comapared with the one next to it.
If the element arr[i] is larger than the next element arr[i + 1], their positions are swapped.
This process is repeated till we achieve a sort.

An outer loop that runs through each element of arr.
An inner loop that comapres each element to the one next to it.
"""

def bubbleSort(arr:list):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

"""
The first algorith works fine but is ineffective because it runs through every element in the array even if they are already sorted
The optimized algo checks if any swaps occur. If no swap happens, the array is sorted and the loop is exited early.
"""

def bubbleSortOptimized(arr:list):
    n = len(arr)

    for i in range(n-1):
        swapped = False # swapped flag to monitor if swapping happened 
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

"""
Time complexity
Worst case -> O(n^2)
Best case -> O(n) (if already sorted)

Space complexity
O(1) (since the sorting happens in-place, no extra space is used up)
"""

# Usage 
arr = [3, 4, 6, 3, 7, 1, 2]
print(f"Sorted: {bubbleSort(arr.copy())}")
print(f"Optimized: {bubbleSortOptimized(arr.copy())}")