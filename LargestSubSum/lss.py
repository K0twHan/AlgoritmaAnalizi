import time
import random

def generate_random_array(n):
    return [random.randint(-100, 100) for _ in range(n)]

def measure_time(method_name, method, arr):
    start_time = time.time()
    result = method(arr)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"{method_name}: {result} (Time: {elapsed_time:.2f} ms)")

def first_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    for start in range(n):
        for end in range(start, n):
            sum_ = sum(arr[start:end + 1])
            max_sum = max(max_sum, sum_)
    return max_sum

def second_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    for start in range(n):
        sum_ = 0
        for end in range(start, n):
            sum_ += arr[end]
            max_sum = max(max_sum, sum_)
    return max_sum

def max_crossing_sum(arr, l, m, h):
    left_sum = float('-inf')
    sum_ = 0
    for i in range(m, l - 1, -1):
        sum_ += arr[i]
        left_sum = max(left_sum, sum_)
    
    right_sum = float('-inf')
    sum_ = 0
    for i in range(m + 1, h + 1):
        sum_ += arr[i]
        right_sum = max(right_sum, sum_)
    
    return max(left_sum + right_sum, left_sum, right_sum)

def max_sum(arr, l, h):
    if l > h:
        return float('-inf')
    if l == h:
        return arr[l]
    
    m = (l + h) // 2
    return max(max_sum(arr, l, m), max_sum(arr, m + 1, h), max_crossing_sum(arr, l, m, h))

def divide_and_conquer(arr):
    return max_sum(arr, 0, len(arr) - 1)

def kadane(arr):
    max_sum = float('-inf')
    sum_ = 0
    for num in arr:
        sum_ += num
        max_sum = max(max_sum, sum_)
        if sum_ < 0:
            sum_ = 0
    return max_sum

if __name__ == "__main__":
    n = 1000  # Change n for different array sizes
    test_array = generate_random_array(n)
    
    measure_time("Kadane’s Algorithm (O(n))", kadane, test_array)
    measure_time("Divide and Conquer (O(n log n))", divide_and_conquer, test_array)
    measure_time("Second Brute Force (O(n²))", second_brute_force, test_array)
    measure_time("First Brute Force (O(n³))", first_brute_force, test_array)
