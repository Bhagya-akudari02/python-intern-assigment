def generate_fib(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    try:
        # Prompt the user to enter the number of terms
        n = int(input("Enter the number Fib sequence: "))

        if n <= 0:
            print("Please enter a positive integer for the number of terms.")
        else:
            # Generate and display the Fibonacci sequence
            fib_sequence = generate_fib(n)
            print(f"Fib sequence up to {n} terms:")
            print(fib_sequence)

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
