# Selection sort implementation

"""
Sorting algorithm where the element with the lowest value is moved to the front of the array.
The idea is to loop through the array and compare each element to the right of the array with the element at position i (initial minimum index)
If the element found is lower than the element at position i, the min index is upated with that position.
After obtaining the min index, the element at that index is popped and inserted to the front of the array.
The rest of the array shifts. 
This process is repeated till we achieve a sort
"""

def selectionSort(arr:list):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        min_value = arr.pop(min_index)
        arr.insert(i, min_value)

    return arr

"""
Inserting an element to the front of the array takes time because of the shift function. 
An optimized method will be to swap the positions of the lowest value with the position i.
"""

def selectionSortOptimized(arr:list):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

"""
Time complexity
Worst case -> O(n^2)

Space complexity
O(1) -> in-place sorting
"""

# Usage
arr = [3, 4, 6, 2, 7, 1, 5]
print(f"Selection sort: {selectionSort(arr.copy())}")
print(f"Optimized selection sort: {selectionSortOptimized(arr.copy())}")