import random

def partition(arr, low, high):
    if randomized:
        pivot = random.randrange(low, high)
        arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot = arr[high]
    i = low - 1 
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1


def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)
        quicksort(arr,low, p-1)
        quicksort(arr, p+1, high)

randomized = bool(input("Random = 1; Determistic = 0; ==> "))

data = [3 ,5, -1, 8, 40, -2, 6]
print("Unsorted data")
print(data)

quicksort(data, 0, len(data)-1)

print("Sorted")
print(data)
