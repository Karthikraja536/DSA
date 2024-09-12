def linearSearch(arr, target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int, input("Enter a list of integers : ").split()))
target = int(input("Enter the target value to search for: "))

result = linearSearch(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")