def fibonacci_up_to_value(max_value):
    """
    Generate a Fibonacci sequence up to a specified maximum value.
    """
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_large_numbers(n):
    """
    Generate the first `n` Fibonacci numbers, handling large numbers.
    """
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci sequence up to a certain value.")
        print("2. Generate Fibonacci sequence with a fixed number of terms (handling large numbers).")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            try:
                max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))
                if max_value < 0:
                    print("Please enter a non-negative number.")
                    continue
                print(f"Fibonacci sequence up to {max_value}:")
                print(fibonacci_up_to_value(max_value))
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == "2":
            try:
                num_terms = int(input("Enter the number of terms: "))
                if num_terms <= 0:
                    print("Please enter a positive integer.")
                    continue
                print(f"Fibonacci sequence with {num_terms} terms:")
                print(fibonacci_large_numbers(num_terms))
            except ValueError:
                print("Invalid input! Please enter an integer.")

        else:
            print("Invalid choice. Please enter 1 or 2.")
