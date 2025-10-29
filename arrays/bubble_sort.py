# implementing a bubble sort 

# sorting algorithm to sort arrays in a way that large element "bubble" up to the top of the array
# that is, each element of the array is comapared with the one next to it
# if the element arr[i] is larger than the next element arr[i + 1], their positions are swapped
# this process is repeated till we achieve a sort

# an outer loop that runs through each element of arr
# an inner loop that comapres each element to the one next to it

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# the first algorith works fine but is ineffective 
# because it runs through every element in the array even if they are already sorted
# the optimized algo checks if any swaps occur
# if no swap happens, the array is sorted and the loop is exited
# basically, it stops early if no swap occurs 

def bubbleSortOptimized(arr):
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


# time complexity
# worst case -> O(n^2)
# best case -> O(n) (if already sorted)

# space complexity
# O(1) (since the sorting happens in-place, no extra space is used up)

# usage 
arr = [3, 4, 6, 3, 7, 1, 2]
print(f"Sorted: {bubbleSort(arr)}")
print(f"Optimized: {bubbleSortOptimized(arr)}")