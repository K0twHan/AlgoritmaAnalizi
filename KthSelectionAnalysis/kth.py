import time
import random

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

def find_kth_smallest_by_sorting(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[k - 1]

def find_kth_smallest_insertion_sort(arr, k):
    k_arr = arr[:k]
    
    # Insertion sort for first k elements
    for i in range(1, k):
        key = k_arr[i]
        j = i - 1
        while j >= 0 and k_arr[j] > key:
            k_arr[j + 1] = k_arr[j]
            j -= 1
        k_arr[j + 1] = key
    
    # Process remaining elements
    for i in range(k, len(arr)):
        if arr[i] < k_arr[k - 1]:
            k_arr[k - 1] = arr[i]
            
            # Re-sort last element using insertion method
            key = k_arr[k - 1]
            j = k - 2
            while j >= 0 and k_arr[j] > key:
                k_arr[j + 1] = k_arr[j]
                j -= 1
            k_arr[j + 1] = key
    
    return k_arr[k - 1]

def measure_time(method_name, method, arr, k):
    start_time = time.time()
    result = method(arr, k)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"({method_name}) {k}th smallest element: {result}, Time: {elapsed_time:.2f} ms")

if __name__ == "__main__":
    arr = generate_random_array(10000000)
    k = 10
    
    measure_time("Full Sort", find_kth_smallest_by_sorting, arr, k)
    measure_time("Partial Sort", find_kth_smallest_insertion_sort, arr, k)
