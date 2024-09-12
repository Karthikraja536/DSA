def SelectionSort(arr):
    for position in range(len(arr)-1):
        min = position
        for i in range(position+1, len(arr)):
            if arr[i] < arr[min]:
                min = i
        arr[min],arr[position] = arr[position],arr[min]
    return arr

arr = list(map(int, input("enter a integer:").split()))
result = SelectionSort(arr)
print(f"Sorted: {result}")
