
def binary_search(arr, x, n):
    lo = 0
    hi = n - 1
    mid = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1
    
arr = [ 2, 3, 4, 10, 15 ]
x = 10
n = len(arr)
result = binary_search(arr, x ,n)

if result == -1:
    print("Element not found")
else:
    print("Element is present at index", str(result))