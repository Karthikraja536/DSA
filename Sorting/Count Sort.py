def  count_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    result = [0] * len(arr)

    for i in range(0, len(arr)):
        count[arr[i]] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(0, len(arr)):
        arr[i] = result[i]
    return arr

arr = list(map(int, input("Enter the elements separated by space: ").split()))
result = count_sort(arr)
print(f"Sorted array: {result}")
