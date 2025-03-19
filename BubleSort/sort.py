import time
import random

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    size_array = [100, 500, 1000, 5000, 10000, 100000, 1000000]
    
    for size in size_array:
        arr = generate_random_array(size)
        start_time = time.time()
        optimized_bubble_sort(arr)
        elapsed_time = (time.time() - start_time) * 1000
        print(f"Sorted array of size {size} in {elapsed_time:.2f} ms")
