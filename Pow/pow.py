call_count = 0  # Global sayaç

def pow_function_linear(x, y):
    global call_count
    result = 1
    
    for _ in range(y):
        call_count += 1
        result *= x
    
    return result

def pow_function_recursive(x, y):
    global call_count
    call_count += 1  
    
    if y == 0:
        return 1
    
    if y % 2 == 1:
        return x * pow_function_recursive(x, y - 1)
    
    m = pow_function_recursive(x, y // 2)
    return m * m

if __name__ == "__main__":
    print("Testing pow_function_linear:")
    call_count = 0
    result_linear = pow_function_linear(2, 16)
    print(f"Result of pow_function_linear: {result_linear}")
    print(f"Function calls in pow_function_linear: {call_count}")
    
    print("\nTesting pow_function_recursive:")
    call_count = 0
    result_recursive = pow_function_recursive(2, 16)
    print(f"Result of pow_function_recursive: {result_recursive}")
    print(f"Function calls in pow_function_recursive: {call_count}")