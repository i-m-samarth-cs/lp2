def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  

        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = list(map(int, input("Enter elements separated by space: ").split()))
print("Before sorting:", arr)

selection_sort(arr) 
print("After sorting:", arr)
