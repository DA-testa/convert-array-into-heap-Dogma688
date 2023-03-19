def sift_down(arr, i, swaps):
    
    n = len(arr)
    min_index = i

    left = 2 * i + 1
    if left < n and arr[left] < arr[min_index]:
        min_index = left

    right = 2 * i + 2
    if right < n and arr[right] < arr[min_index]:
        min_index = right

    if i != min_index:
        swaps.append((i, min_index))
        arr[i], arr[min_index] = arr[min_index], arr[i]
        sift_down(arr, min_index, swaps)


def build_heap(arr):


    n = len(arr)
    swaps = []

    for i in range(n // 2, -1, -1):
        sift_down(arr, i, swaps)

    return swaps


n = int(input())
arr = list(map(int, input().split()))

swaps = build_heap(arr)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])
