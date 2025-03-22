import random

def bubble_sort_unoptimized(arr):
    n = len(arr)
    arr_copy = arr[:]
    number_of_comparisons = 0
    
    for i in range(n - 1):
        for j in range(n - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
            number_of_comparisons += 1
    
    return number_of_comparisons

def bubble_sort_optimized(arr):
    n = len(arr)
    arr_copy = arr[:]
    number_of_comparisons = 0
    
    for i in range(n - 1):
        no_swap = True
        for j in range(n - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                no_swap = False
            number_of_comparisons += 1
        if no_swap:
            break
    
    return number_of_comparisons

if __name__ == "__main__":
    sorted_array = [3, 4, 5, 6, 10, 12, 15, 20, 23, 100]
    unsorted_array = [12, 3, 6, 4, 10, 5, 11, 7, 9, 8]
    n = len(sorted_array)
    print(f"Size n: {n}\n")
    
    print(f"Unoptimized Bubble Sort O value: {bubble_sort_unoptimized(unsorted_array)}")
    print(f"Optimized Bubble Sort O value: {bubble_sort_optimized(unsorted_array)}")
    print()
    print(f"Unoptimized Bubble Sort Delta value: {bubble_sort_unoptimized(sorted_array)}")
    print(f"Optimized Bubble Sort Delta value: {bubble_sort_optimized(sorted_array)}")
    print()
    
    trials = 100
    total_unoptimized = 0
    total_optimized = 0
    
    for _ in range(trials):
        random_array = [random.randint(1, 100) for _ in range(n)]
        total_unoptimized += bubble_sort_unoptimized(random_array)
        total_optimized += bubble_sort_optimized(random_array)
    
    print(f"Average comparisons (Unoptimized Bubble Sort): {total_unoptimized / trials}")
    print(f"Average comparisons (Optimized Bubble Sort): {total_optimized / trials}")
