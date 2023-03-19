def heapify(arr, n, i):

    largest = i 
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        heapify(arr, n, largest)

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

print("The heapified array is: ")
for i in range(n):
    print(arr[i], end=" ")
