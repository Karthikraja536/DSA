def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    return -1

arr = list(map(int, input("Enter sorted list of integers : ").split()))
target = int(input("Enter the target value to search for: "))

result = binarySearch(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")