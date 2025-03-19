def min_function(arr):
    control = 1
    min_value = arr[0]
    for i in range(1, len(arr)):
        control += 1
        if arr[i] < min_value:
            min_value = arr[i]
    return control

def max_function(arr):
    control = 1
    max_value = arr[0]
    for i in range(1, len(arr)):
        control += 1
        if arr[i] > max_value:
            max_value = arr[i]
    return control

def linear_search(arr, value):
    control = 0
    for i in range(len(arr)):
        control += 1
        if arr[i] == value:
            break
    return control

def binary_search(arr, value):
    arr_cpy = sorted(arr)
    control = 0
    left, right = 0, len(arr_cpy) - 1
    
    while left <= right:
        control += 1
        mid = (left + right) // 2
        if value > arr_cpy[mid]:
            left = mid + 1
        elif value < arr_cpy[mid]:
            right = mid - 1
        else:
            break
    
    return control

if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
    unsorted_array = [8, 5, 3, 2, 7, 6, 4, 1]
    search_value = 7
    
    print("N is:", len(sorted_array))
    print()
    
    print("Testing Min Function:")
    print("Best Case (First Element is Min):", min_function(sorted_array))
    print("Worst Case (Last Element is Min):", min_function(unsorted_array))
    
    print("\nTesting Max Function:")
    print("Best Case (First Element is Max):", max_function(sorted_array[::-1]))
    print("Worst Case (Last Element is Max):", max_function(unsorted_array[::-1]))
    
    print("\nTesting Linear Search:")
    print("Best Case (First Element Match):", linear_search(sorted_array, sorted_array[0]))
    print("Worst Case (Last Element Match):", linear_search(sorted_array, sorted_array[-1]))
    print("Average Case (Middle Element Match):", linear_search(sorted_array, sorted_array[(len(sorted_array) - 1) // 2]))
    
    print("\nTesting Binary Search:")
    print("Best Case (Middle Element Match):", binary_search(sorted_array, sorted_array[(len(sorted_array) - 1) // 2]))
    print("Worst Case (Not Found Case):", binary_search(sorted_array, 100))
    print("Average Case (Random Element Match):", binary_search(sorted_array, search_value))
    #