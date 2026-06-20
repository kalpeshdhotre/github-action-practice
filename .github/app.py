def print_fibonacci(n):
    # Handle edge case for non-positive input
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    # Initialize the first two terms
    a, b = 0, 1
    
    print(f"Fibonacci series with {n} elements:")
    for _ in range(n):
        print(a, end=" ")
        # Update values simultaneously using tuple unpacking
        a, b = b, a + b
    print()  # Newline

# Example usage: Generate the first 10 numbers
print_fibonacci(10)
