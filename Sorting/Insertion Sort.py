def InsertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1     #arr[0]

        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr
arr = list(map(int, input("enter a integer:").split()))
result = InsertionSort(arr)

print(f"Sorted: {result}")
